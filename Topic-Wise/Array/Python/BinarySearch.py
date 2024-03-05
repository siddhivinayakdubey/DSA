def BinarySearch(A,T):
    first=0
    last=len(A)-1

    while first<=last:
        mp=(first+last)//2

        if A[mp]==T:
            return mp
        elif T<A[mp]:
            last=mp-1
        elif T>A[mp]:
            first=mp+1
    return None

A=[1,2,3,4,5,6,7,8,9,10]
T=10

print(BinarySearch(A,T))


