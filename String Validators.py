if __name__ == '__main__':
    s = input()
alnum=0
alpha=0
digit=0
lower=0
upper=0    
for i in range(len(s)):
    if(s[i].isalnum()):
        alnum+=1
    if(s[i].isalpha()):
        alpha+=1
    if(s[i].isdigit()):
        digit+=1
    if(s[i].islower()):
        lower+=1
    if(s[i].isupper()):
        upper+=1
print(alnum>0)
print(alpha>0)
print(digit>0)
print(lower>0)
print(upper>0)