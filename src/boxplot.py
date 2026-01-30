import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Load the California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Create the figs directory if it doesn't exist
os.makedirs("figs", exist_ok=True)

# Create a boxplot for Median Income
plt.figure(figsize=(6, 4))
plt.boxplot(df["MedInc"], vert=True)
plt.title("Boxplot of Median Income")
plt.ylabel("Median Income")

# Save the figure
plt.savefig("figs/boxplot.png")
plt.close()

print("Boxplot saved to figs/boxplot.png")
