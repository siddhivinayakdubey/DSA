
def palindromeNumber(x):
    if x<0:
        return False
    else:
        n=abs(x)
        rev=0
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10

        if rev==x:
            return True
        else:
            return False

print(palindromeNumber(0))
