import numpy as np

with open("test.txt", "r") as f:
    data = f.read().split("\n\n")
    data = [element.split() for element in data]

R = []
T = []
J = []

for i in range(0, len(data)):
    if i % 3 == 0:
        R += [float(j.strip()) for j in data[i]]
    if i % 3 == 1:
        T += [float(j.strip()) for j in data[i]]
    if i % 3 == 2:
        J += [float(j.strip()) for j in data[i]]

np.savetxt("test.csv", np.array([R, T, J]).transpose(), delimiter=",", fmt="%.2f")
