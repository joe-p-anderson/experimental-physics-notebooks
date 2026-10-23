import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

hdrop = data['h (m)'].to_numpy()
tfall = data['tfall (s)'].to_numpy()

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111)

plt.scatter(hdrop, tfall, color='blue', label='Data points')

