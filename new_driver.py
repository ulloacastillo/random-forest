from RandomForest import RandomForestClassifier
import pandas as pd
import pickle
from motivus.client import Client
import asyncio
import time
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


data = load_breast_cancer()

X = data.data
y = list(map(str, data.target))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=41)


# n_estimators=100, min_samples_split=2, max_depth=3, n_features=4, seed=41)


rf = RandomForestClassifier(
    n_estimators=100, min_samples_split=2, max_depth=3, n_features=4, seed=41)


rf.fit(X_train.tolist(), y_train)
#pred = rf.predict(y_test.tolist())
