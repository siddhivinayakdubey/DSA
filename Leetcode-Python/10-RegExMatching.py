def isMatch(s,p):
    s=list(s)
    p=list(p)
    n=len(s)
    flag=0
    i=0
    j=0

    while i<n:
        if s[i]!=p[j]:
            if p[j]=='.' and flag==0:
                print("rinning for dot")
                flag=1

            if s[i]!=s[i-1]:
                flag=0

            if p[j]=='*':
                print("runnnig")
                temp=p[j-1]
                while s[i]!=temp:
                    i+=1
            else:
                return False

        i+=1
        j+=1
    return True


s='aa'
p='a.'

print(isMatch(s,p))
