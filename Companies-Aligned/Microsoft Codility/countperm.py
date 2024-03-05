# A non-empty array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and only once.
#
# For example, array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.
#
# Given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].
# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(A):
    # write your code in Python 3.6
    # size = max(A)
    # count = size
    # H = [False] * (size + 1)
    #
    # for i in range(0, len(A)):
    #     if (H[A[i]] == True):
    #         return 0
    #     if (H[A[i]] == False):
    #         H[A[i]] = True
    #         count -= 1
    #         if (count == 0):
    #             return 1
    # return 0

    A.sort()
    if (len(A) == max(A)):
        count = 1
        for i in range(0, len(A)):
            if A[i] == count:
                count += 1
            else:
                return 0
        return 1
    return 0
array=[1,1]
print(solution(array))
