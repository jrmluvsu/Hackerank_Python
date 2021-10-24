def minion_game(string):
    # your code goes here
    count1, count2 = 0, 0
    size = len(string)
    for i in range(size):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            count1 += (size-i)
        else:
            count2 += (size-i)
    if count2 > count1:
        print("Stuart", count2)
    elif count1 > count2:
        print("Kevin", count1)
    else:
        print("Draw")