def maxset(A):
    i = 0
    sum = 0
    Max = -1
    n = len(A)
    maxarr = []
    temparr = []

    for i in range(0, n):
        if A[i] < 0:
            i += 1
            temparr = []
            sum=0
        else:
            sum += A[i]
            temparr.append(A[i])

            if sum > Max:
                Max = sum
                maxarr = temparr

            else:
                temparr = []
                sum = 0

    return maxarr
A =[ 1, 2, 5, -7, 2, 7 ]
print(maxset(A))

[1,-1,]
