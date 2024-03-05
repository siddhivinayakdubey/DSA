def solution(s):
    s=list(s)
    maxi=0
    count=0
    check=set()
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    else:
        i=0
        j=0
        while i<=len(s) and j<len(s):
            print(s[i])

            if s[j] not in check:
                print("new element "+s[j])
                count+=1
                print(count)
                check.add(s[j])
                j=j+1
            elif s[j] in check:
                print("clearning")
                check.clear()
                count=0
                i+=1
                j=i

            if count > maxi:
                maxi = count
                print("maxi: " + str(maxi))


        return maxi




s="abcabcbb"
print(solution(s))




