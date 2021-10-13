l=[]
n=int(input())

for i in range(n):
    cmd=input().split()
    if 'insert' in cmd:
        l.insert(int(cmd[1]),int(cmd[2]))
    elif 'print' in cmd:
        print(l)
    elif 'remove' in cmd:
        l.remove(int(cmd[1]))
    elif 'append' in cmd:
        l.append(int(cmd[1]))
    elif 'reverse' in cmd:
        l=l[::-1]
    elif 'pop' in cmd:
        l.pop()
    else:
        l.sort()