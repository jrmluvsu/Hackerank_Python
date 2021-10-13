n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
l=set(l)
count=len(l)
print (count)