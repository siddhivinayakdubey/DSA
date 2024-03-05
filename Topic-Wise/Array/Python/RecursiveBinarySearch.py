def RecursiveBinarySearch(A,T):
    mp=len(A)//2
    if len(A)==0:
        return False
    if A[mp]==T:
        return True
    elif A[mp]<T:
        return RecursiveBinarySearch(A[mp+1:],T)
    elif A[mp]>T:
        return RecursiveBinarySearch(A[:mp],T)


A=[1,2,3,4,5,6,7,8,9,10]
T=51

print(RecursiveBinarySearch(A,T))

