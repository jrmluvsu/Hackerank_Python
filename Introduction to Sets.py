def average(array):
    sum=0
    count=0
    array=list(set(array))
    for i in range(len(array)):
        sum+=array[i]
        count+=1
    return sum/count