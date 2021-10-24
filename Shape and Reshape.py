import numpy as np
l = list(map(int, input().split()))
arr = np.reshape(np.array(l), (3, 3))
print(arr)