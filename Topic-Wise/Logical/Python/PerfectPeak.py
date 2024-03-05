def perfectPeak(A):
    count = 0
    n = len(A)
    for i in range(0, n):
        for j in range(0, i - 1):
            for k in range(i + 1, n):
                if A[j] > A[i] and A[k] < A[i]:
                    count += 1
                    j += 1
                    k += 1
                else:
                    j+=1
                    k+=1
    return count
A = [ 5706, 26963, 24465, 29359, 16828, 26501, 28146, 18468, 9962, 2996, 492, 11479, 23282, 19170, 15725, 6335 ]

print(perfectPeak(A))