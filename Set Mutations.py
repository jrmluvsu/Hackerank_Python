n = int(input())
a = set(map(int, input().split()))
for i in range(int(input())):
    s, num = input().split()
    l = set(map(int, input().split()))
    if s == 'update':
        a.update(l)
    elif s == 'intersection_update':
        a.intersection_update(l)
    elif s == 'difference_update':
        a.difference_update(l)
    elif s == 'symmetric_difference_update':
        a.symmetric_difference_update(l)
print(sum(a))