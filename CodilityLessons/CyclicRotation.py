def sol(A,K):
    if len(A)==0:
        return 0
    else:

        n=len(A)
        x=K%len(A)

        arr1=A[:n-x]
        arr2=A[n-x:]
        final=arr2+arr1
        return final
A=[3,8,9,7,6]
K=2
print(sol(A, K))
