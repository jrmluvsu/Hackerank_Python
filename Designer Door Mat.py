n, m = map(int, input().split())
for i in range(1, n//2+1):
    x = 2*i-1
    print('-'*((m-(3*x))//2), end='')
    print('.|.'*x, end='')
    print('-'*((m-(3*x))//2))
print('-'*((m-7)//2), end='')
print('WELCOME',end='')
print('-'*((m-7)//2))
for i in range(n//2, 0, -1):
    x = 2*i-1
    print('-'*((m-(3*x))//2), end='')
    print('.|.'*x, end='')
    print('-'*((m-(3*x))//2))