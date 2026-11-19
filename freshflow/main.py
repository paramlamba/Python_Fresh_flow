import numpy as np
with open("freshflow_sales.csv", "r") as file:
    header = file.readline().strip().split(",")
    data = np.loadtxt(file, delimiter=",")
print("dataset shape", data.shape)
print("upper 5 rows")
print(data[:5])
print(data[5:])
print("lower 5 rows")
print("Total Rows", data.shape[0])
print("Total Columns", data.shape[1])
data = data[~np.isnan(data).any(axis=1)]
np.savetxt("freshflow_sales.csv.csv", data)
print("Missing values removed")
print(data)
