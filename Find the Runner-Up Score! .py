a=int(input())
l=[]
b=input().split()
for i in range(a):
    l.append(int(b[i]))
l.sort()
s=l[a-1]
for i in range(1,a+1):
    num=l[a-i]
    if num==s:
        continue
    else:
        break
print(num)