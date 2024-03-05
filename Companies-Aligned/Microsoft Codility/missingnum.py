# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

A=[1, 3, 6, 4, 1, 2]
def solution(A):
    # write your code in Python 3.6
    A.sort()
    n = len(A)
    if (A[n - 1] <= 0):
        return 1
    else:
        pointer = 0
        while (A[pointer] <= 0):
            pointer += 1

        if (A[pointer] != 1):
            return 1

        arr = A[pointer:]
        m = len(arr)

        maxele = max(arr)

        H = [False] * (maxele + 1)
        for i in range(0, m):
            if (H[arr[i]] == False):
                H[arr[i]] = True

        for j in range(1, len(H)):
            if H[j] == False:
                return j
        return j+1

print(solution(A))