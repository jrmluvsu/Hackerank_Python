if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[num1, num2, num3] for num1 in range(x+1) for num2 in range(y+1) for num3 in range(z+1) if (num1+num2+num3) != n]
    print(l)