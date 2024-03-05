def subUnsort( A):
    B = sorted(A)
    n = len(A)
    arr = []

    if A == B:
        return int(-1)
    else:
        for i in range(0, n - 1):
            if A[i] == B[i]:
                continue
                i += 1
            elif A[i] != B[i]:
                if B[i] == A[i - 1]:
                    continue
                else:
                    arr.append(B[i - 1])
                    arr.append(B[i])
        return arr

A=[1,3,2,4,5]
print(subUnsort(A))