# SC2001/lab1/graphs/cii_comparisons_fixed_N_diff_S.py
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

# Load data and assign column name 
hybrid_data = pd.read_csv("lab1/hybrid.csv", header = None, names = ["n", "s", "time", "comparisons"])

# Fix value of N
N = 100000

# Retrieve relevant rows 
data = hybrid_data[hybrid_data["n"] == N].sort_values("s")
s_values = np.array(data["s"])

# Calculate Theoretical # Key Comparisons using derived formula
theoretical_kc = N * np.log2(N/s_values) + (N / (4*s_values)) * (s_values - 1) * (s_values + 2)

# Plot 
plt.plot(s_values, data["comparisons"] / 1000000, label = "Empirical", color = "blue")
plt.plot(s_values, theoretical_kc / 1000000, label = "Theoretical", color = "red")

plt.title(f"Number of Key Comparisons vs S Values (N = {N})")
plt.xlabel("S Value")
plt.ylabel("Number of Key Comparisons (Millions)")
plt.legend()
plt.show()

