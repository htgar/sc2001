# SC2001/lab1/graphs/ciii_optimal_S.py
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

# Load data and assign column name 
hybrid_data = pd.read_csv("lab1/hybrid.csv", header = None, names = ["n", "s", "time", "comparisons"])

# For each n value, find: 1) the S with lowest # key comparisons, 2) the S with lowest Run Time
best_s_per_n_comp = []
best_s_per_n_time = []

for n in sorted(hybrid_data["n"].unique()):
    # Fetch all hybrid rows with this n value
    hybrid_rows = hybrid_data[hybrid_data["n"] == n]

    # Get the row with least # key comparisons 
    best_row_comp = hybrid_rows.loc[hybrid_rows["comparisons"].idxmin()]
    # save as (n, bestS) pair 
    best_s_per_n_comp.append((n, best_row_comp["s"]))

    # Get the row with the least runtime 
    best_row_time = hybrid_rows.loc[hybrid_rows["time"].idxmin()]
    best_s_per_n_time.append((n, best_row_time["s"]))

# Save each pair into 2 different lists 
n_vals_comp, s_vals_comp = zip(*best_s_per_n_comp)
n_vals_time, s_vals_time = zip(*best_s_per_n_time)

mode_s_comp = pd.Series(s_vals_comp).mode()[0]
mode_s_time = pd.Series(s_vals_time).mode()[0]

# Plot
plt.scatter(np.array(n_vals_comp) / 1000000, s_vals_comp, color = "blue", label = "Best S (min comparisons)")
plt.scatter(np.array(n_vals_time) / 1000000, s_vals_time, color = "red", label = "Best S (min time)")

plt.axhline(mode_s_comp, color = "blue", linestyle = "--", label = f"Mode of Optimal S (comparisons) = {mode_s_comp:.3g}")
plt.axhline(mode_s_time, color = "red", linestyle = "--", label = f"Mode of Optimal S (time) = {mode_s_time:.3g}")

plt.title("Optimal Threshold S vs Input Size")
plt.xlabel("Input Size, n (Millions)")
plt.ylabel("Optimal S")
plt.yscale("log", base=2)
plt.yticks(sorted(hybrid_data["s"].unique()))
plt.legend()
plt.show()