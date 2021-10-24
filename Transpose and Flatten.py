import numpy as np

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
arr = np.array(l)
print(arr.T)
print(arr.flatten())