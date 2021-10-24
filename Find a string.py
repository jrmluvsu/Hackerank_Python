def count_substring(string, sub_string):
    s=0
    for i in range(len(string)-len(sub_string)+1):
            if sub_string==string[i:len(sub_string)+i]:
                s+=1
    return s