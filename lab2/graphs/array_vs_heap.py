import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("results.csv")

density = 2*df['E'] / (df['V'] * (df['V'] - 1))
ratio = df['Array_Time'] / df['Heap_Time']

plt.scatter(density, ratio, alpha=0.6)
plt.axhline(1, color='k', linestyle='--')
plt.xlabel('Density (E / V^2)')
plt.ylabel('Array / Heap runtime')
plt.title('Array vs Heap')
plt.grid(True, ls=':')
plt.show()