import numpy as np
import pandas as pd
import pickle
from motivus.client import Client
import asyncio
import time
import random
from datetime import datetime

# libreria timeit

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

for j in range(3):
    for i in range(100, 3001, 100):
        task_type = "train"  # can be train or predict

        par = {'n_trees': 1, 'min_samples_split': 2,
               'max_depth': 0, 'n_feats': 10, 'seed': 41}

        task_definition = {
            'wasm_path': "build/random-forest-0.1.5.wasm",
            'loader_path': "build/random-forest-0.1.5.js",
            # 'algorithm': "random-forest",
            # 'algorithm_version': "0.1.3",
            'params': [par, X[:i], y[:i], task_type]
        }

        async def main():
            motivus = await Client.connect()
            task_id = motivus.call_async(task_definition)
            task = motivus.select_task(task_id)

            return await task

        start = time.time()

        result = asyncio.run(main())

        exc_time = time.time() - start

        if task_type == "train":
            with open('random_forest.pickle', 'wb') as file:
                pickle.dump(result, file, protocol=pickle.HIGHEST_PROTOCOL)

            with open("train_times.csv", "a") as file:
                file.write(
                    f"\n{i},{exc_time},{par['n_trees']},{par['min_samples_split']},{par['max_depth']},{par['n_feats']}")

        print(f"Execution time: {exc_time} seconds")
