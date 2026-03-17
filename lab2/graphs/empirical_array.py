import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

df = pd.read_csv("results.csv")
df = df[df['Density'] == 0.5]

x = df['V']
y = df['Array_Time']

df = df.assign(x=x, y=y).sort_values(by='x')
x = df['x']
y = df['y']

log_x = np.log(x)
log_y = np.log(y)

slope, intercept, _, _, _ = linregress(log_x, log_y)
log_y_fit = slope * log_x + intercept

plt.plot(log_x, log_y, 'o', label='Measured')
plt.plot(log_x, log_y_fit, '-', label=f'Fit: slope={slope:.2f}')

plt.xlabel("log(V)")
plt.ylabel("log(Runtime)")
plt.title("Array Dijkstra (Log-Log)")
plt.legend()
plt.grid(True)
plt.show()