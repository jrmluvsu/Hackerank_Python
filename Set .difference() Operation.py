a=int(input())
b=input().split()
c=int(input())
d=input().split()
e=set(map(int,b))
f=set(map(int,d))
g=e.difference(f)
print(len(g))