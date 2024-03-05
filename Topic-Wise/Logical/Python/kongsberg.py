import math

def comb(m,n):
    # //m=stalls
    # n=days
    arr=[]
    for i in range(1,n+1):
        x=math.factorial(m)/((math.factorial(i)*math.factorial((abs(m-i)))))
        arr.append(x)
    sums=(int)(sum(arr))
    return sums

print(comb(4,2))
