a=int(input())
b=input().split()
c=int(input())
d=input().split()
e=set(map(int,b))
f=set(map(int,d))
g=e.symmetric_difference(f)
print(len(g))