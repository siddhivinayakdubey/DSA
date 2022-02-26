from collections import Counter
def sol(A):
    c=Counter(A)
    for i in range(0,len(A)):
        if c[A[i]]%2!=0:
            return A[i]

x=3/2.
print(round(3/2))