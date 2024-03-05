import math
def reverseInteger(x):
    n=abs(x)
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev>=math.pow(2,-31) and rev<=math.pow(2,31):
        if x<0:
            return -rev
        else:
            return rev
    else:
        return 0

print(reverseInteger(1534236469))
