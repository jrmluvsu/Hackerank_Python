import numpy as np
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
a = np.array(a)
b = np.array(b)
print(np.dot(a, b))