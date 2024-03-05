
def isPrime(n):
    if n==1:
        return True
    if n==2:
        return True
    else:
        for i in range(1,n):
            if(n%i==0):
                return False
            else:
                return True
def PalindromeCheck(n):
    x=int(n)
    rev=int(0)
    while(n>0):
        r=(int)(n%10)
        rev=rev*10+r
        n=(int)(n/10)
    if rev==x:
        return True

num=121
for i in range(1,num):
    if(isPrime(i)==True and PalindromeCheck(i)==True):
        print(i)

