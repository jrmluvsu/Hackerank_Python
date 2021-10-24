import numpy as np
n, m, p = map(int, input().split())
l1, l2 = [], []
for i in range(n):
    l1.append(list(map(int, input().split())))
for i in range(m):
    l2.append(list(map(int, input().split())))
print(np.concatenate((np.array(l1), np.array(l2)), axis=0))