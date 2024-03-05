def Evensum(n):
    sum=0
    for i in range(0,n,2):
        sum = i+sum

    return sum

Evensum(6)