def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string)//k):
        s=""
        for j in string[i*k:i*k+k]:
            if j not in s:
                s+=j
        print(s)
    return None