target = list(map(int, input().split()))
# def khushi(target):
#     final=0
#     n=len(target)
#
#     while(True):
#         zcount = 0
#         i = 0
#         while (i < n):
#             if ((target[i] & 1) > 0):
#                 break
#             elif (target[i] == 0):
#                 zcount += 1
#             i += 1
#         if (zcount == n):
#             return final
#         if (i == n):
#             for j in range(n):
#                 target[j] = target[j] // 2
#             final += 1
#         for j in range(i, n):
#             if (target[j] & 1):
#                 target[j] -= 1
#                 final += 1
# print(khushi(target))
target.sort()
n=len(target)
print(target[n-1]+target[n-2])


5
6 4 2 3 9

6
-3 5 -6 9 8 -9