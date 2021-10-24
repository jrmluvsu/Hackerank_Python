def print_formatted(number):
    # your code goes here
    pad2 = len(bin(number)[2:])+1
    for i in range(1, number+1):
        print(' '*(pad2-len(str(i))-1)+str(i), end='')
        print(' '*(pad2-len(oct(i)[2:]))+oct(i)[2:], end='')
        print(' '*(pad2-len(hex(i)[2:]))+hex(i)[2:].upper(), end='')
        print(' '*(pad2-len(bin(i)[2:]))+bin(i)[2:], end='')
        print()