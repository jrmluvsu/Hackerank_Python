import numpy as np
n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
a = np.array(a)
b = np.array(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)