def solution(s):
    v=s
    s=list(s)
    max=0
    x=set(s)
    maxstring=[]
    if len(s)==1:
        return v
    if len(x)==1:
        return v
    if len(s)==2 and s[0]!=s[1]:
        return s[0]

    m=0
    n=m+1
    # FOR EVEN
    while n<len(s):
        if s[m]==s[n]:
            arr1=s[:n]
            arr2=s[n:]
            i=len(arr1)-1
            j=0
            count=0
            while arr1[i]==arr2[j] and i>=0 and j<len(arr2):
                count+=2

                i-=1
                j+=1
                if i<0 or j>=len(arr2):
                    break


            if count>max:
                max=count
                maxstring=arr1[i+1:]+arr2[:j]


        m+=1
        n+=1

    # FOR ODD
    i=0
    j=i-1
    k=i+1

    while k<len(s):
        if(s[j]==s[k]):
            arr1=s[:k]
            arr2=s[k:]

            m = len(arr1) - 2
            n = 0
            count = 0
            while arr1[m] == arr2[n] and m >= 0 and n < len(arr2):
                count += 2
                m -= 1
                n += 1
                if m <= 0 or n >= len(arr2):
                    break

            if count > max:
                max = count+1

                maxstring = arr1[m + 1:] + arr2[:n]

        i+=1
        j+=1
        k+=1

    result=''.join([str(ele) for ele in maxstring])
    return result



s="cc"

print(solution(s))

