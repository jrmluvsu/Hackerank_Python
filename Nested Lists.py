if __name__ == '__main__':
    l = []
    l2 = []
    l1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    for i in l:
        l2.append(i[1])
    uni = list(set(l2))
    uni = sorted(uni)
    req = uni[1]

    for i in l:
        if i[1] == req:
            l1.append(i[0])
    l1 = sorted(l1)
    for name in l1:
        print(name)