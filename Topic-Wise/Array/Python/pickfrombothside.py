A=[17,2,1,4,0,5]
B=3
n=len(A)
sum=sum(A[:B])
# sum2=sum(A[])

for i in reversed(range(B)):
    sum += -A[i] + A[i - B]
print(sum)


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         current_sum = sum(A[:B])
#         max_sum = current_sum
#         if B < len(A):
#             for i in reversed(range(B)):
#                 current_sum += -A[i] + A[i - B]
#                 if current_sum > max_sum:
#                     max_sum = current_sum
#         return max_sum


# def solve(A, B):
#     sum = 0
#     n = len(A)
#     i = 0
#     for n in range(1, B):
#         if A[i] > A[n]:
#             sum = sum + A[i]
#             i = i + 1
#         else:
#             sum = sum + A[n]
#             n = n - 1
#
#     return sum
#
#
# solve([17,2,1,4,0,5],3)
# print(sum)