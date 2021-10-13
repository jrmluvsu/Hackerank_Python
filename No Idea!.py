n, m = map(int, input().split())
s = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
total = 0
for i in s:
    if i in A:
        total += 1
    if i in B:
        total -= 1
print(total)