import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
weekly = pd.read_csv('/home/knowusuboaky/dataset-95529.csv')
fig = plt.figure(figsize = (10, 8))
ax = plt.axes()
ax.scatter(x = weekly.index, y = weekly["Volume"], alpha = 0.5)
ax.set(xlabel='Year', ylabel='Volume', title='Scatter Plot of Volume and Year')
ax.grid()
fig.savefig("graphical_correlation_analysis.png")
plt.show()
