"""
Sandbox for experimenting with DataFrames

Use this file to try out different DataFrame operations
as you work through the lab.
"""

import pandas as pd

# Example: Create a simple DataFrame
df = pd.read_csv("labs/lab09/data/students.csv")

max = df["Math"].max()
print(df.loc[df["Math"] == max, "Name"])