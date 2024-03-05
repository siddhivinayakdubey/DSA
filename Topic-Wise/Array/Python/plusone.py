A=[1,2,3,4]
n=len(A)

for i in range(1,n):
    A[0] = 10 * A[0] + A[i]
print(A)


