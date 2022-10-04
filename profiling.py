import numpy as np
import pandas as pd
import pickle
from motivus.client import Client
import asyncio
import time
import random
from datetime import datetime


N_SAMPLES = 10000
N_FEATS = 100
N_CLASSES = 20
DATASET_SIZE = 100

# X = np.random.rand(N_SAMPLES, N_FEATS)
# y = np.random.randint(N_CLASSES, size=(N_SAMPLES, 1))
# matrix = np.concatenate((X, y), axis=1)
# df = pd.DataFrame(matrix)
# df.to_csv("data.csv")

df = pd.read_csv("data.csv", index_col=0)

X = df.iloc[:, :-1].values.tolist()
y = list(map(str, df.iloc[:, -1:].values.reshape(N_SAMPLES, ).tolist()))


task_type = "train"  # can be train or predict

par = {'n_trees': 1, 'min_samples_split': 3,
       'max_depth': 50, 'n_feats': 10, 'seed': 41}

task_definition = {
    'wasm_path': "build/random-forest-0.1.3.wasm",
    'loader_path': "build/random-forest-0.1.3.js",
    # 'algorithm': "random-forest",
    # 'algorithm_version': "0.1.3",
    'params': [par, X[:DATASET_SIZE], y[:DATASET_SIZE], task_type]
}


async def main():
    motivus = await Client.connect()
    task_id = motivus.call_async(task_definition)
    task = motivus.select_task(task_id)

    return await task


start = time.time()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

result = asyncio.run(main())

if task_type == "train":
    with open('random_forest.pickle', 'wb') as file:
        pickle.dump(result, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(result)

    exc_time = time.time() - start

    with open("train_times.csv", "a") as file:
        file.write(
            f"\n{DATASET_SIZE},{exc_time},{dt_string},{par['n_trees']},{par['min_samples_split']},{par['max_depth']},{par['n_feats']}")

print(f"Execution time: {exc_time} seconds")
