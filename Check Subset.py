t = int(input())
for _ in range(t):
    n_A = int(input())
    A = list(map(int, input().split()))
    n_B = int(input())
    B = list(map(int, input().split()))
    for i in A:
        if i not in B:
            print("False")
            break
    else:
        print("True")