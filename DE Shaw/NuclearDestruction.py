# import sys
# def solution(a):
#     mini=sys.maxsize
#
#     for i in range(0,len(a)):
#         destructions=0
#         for j in range(0,len(a)):
#             if a[j]>=a[i]:
#                 destructions+=abs(a[i]-a[j])
#             else:
#                 destructions+=a[j]
#         if destructions<mini:
#             mini=destructions
#     return mini


import sys
def solution(a):
    mini=sys.maxsize
    i=0
    j=0
    destructions=0
    while i<len(a):
        if j<len(a):
            if a[j] >= a[i]:
                destructions += (a[j] - a[i])
                j+=1
            else:
                destructions += a[j]
                j+=1
        elif j==len(a):

            if destructions<mini:
                mini=destructions
            destructions=0
            j=0
            i+=1
    return mini
a=[1,2]
print(solution(a))
