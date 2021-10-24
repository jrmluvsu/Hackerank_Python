import numpy as np
r, c = map(int, input().split())
l = []
for i in range(r):
    l.append(list(map(int, input().split())))
arr = np.array(l)
print(np.max(np.min(arr, axis=1)))