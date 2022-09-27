import pandas as pd
import pickle
from motivus.client import Client
import asyncio
import time
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=41)

task_type = "train"  # can be train or predict

params = {'n_trees': 100, 'min_samples_split': 3,
          'max_depth': 3, 'n_feats': 4, 'seed': 41}

task_definition = {
    'algorithm': "random-forest",
    'algorithm_version': "0.1.2",
    'params': [params, X, y, task_type]
}


async def main():
    motivus = await Client.connect()
    task_id = motivus.call_async(task_definition)
    task = motivus.select_task(task_id)

    return await task


result = asyncio.run(main())
