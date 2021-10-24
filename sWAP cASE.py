def swap_case(s):
    l1 = s.split()
    for word in range(len(l1)):
        l = [i.upper() if i.islower() else i.lower() for i in l1[word]]
        l1[word] = "".join(l)
    return " ".join(l1)