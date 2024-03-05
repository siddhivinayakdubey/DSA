def solve(A):
    n = len(A)
    for i in range(0, n):
        A[i] = A[i] * A[i]
    A = sorted(A)
    return A
A=[3,5,6,7]
print(solve(A))


