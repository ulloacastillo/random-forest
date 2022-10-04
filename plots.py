import matplotlib.pyplot as plt
import pandas as pd
#from pandasql import sqldf


df = pd.read_csv("train_times.csv").drop(columns=['date'])

print(df.head())

fig, ax = plt.subplots()

ax.scatter(df['datasize'], df['ex_time[s]'])
plt.xlabel("Samples/Dataset")
plt.ylabel("Time[s]")

plt.show()
