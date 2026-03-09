# SC2001/lab1/graphs/ci_comparisons_fixed_S_diff_N.py
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

# Load data and assign column name 
hybrid_data = pd.read_csv("lab1/hybrid.csv", header = None, names = ["n", "s", "time", "comparisons"])

# Fix value of S 
S = 8 

# Retrieve relevant rows 
data = hybrid_data[hybrid_data["s"] == S].sort_values("n")
n_values = np.array(data["n"])

# Calculate Theoretical # Key Comparisons using derived formula
theoretical_kc = n_values * np.log2(n_values / S) + (n_values / (4*S)) * (S - 1) * (S + 2)

# Plot 
plt.plot(n_values / 1000000, data["comparisons"] / 1000000, label = "Empirical", color = "blue")
plt.plot(n_values / 1000000, theoretical_kc / 1000000, label = "Theoretical", color = "red")

plt.title(f"Number of Key Comparisons vs Input Size (S = {S})")
plt.xlabel("Input Size, n (Millions)")
plt.ylabel("Number of Key Comparisons (Millions)")
plt.legend()
plt.show()

