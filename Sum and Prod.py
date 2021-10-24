import numpy as np
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l = np.array(l)
print(np.prod(np.sum(l, axis=0), axis=0))