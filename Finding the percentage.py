n=int(input())
dict={}
for i in range(n):
    a=input().split(" ")
    dict[a[0]]=(float(a[1])+float(a[2])+float(a[3]))/3
s=input()
print('%.2f'%dict[s])