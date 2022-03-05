import sys
def solution(a):
    mini=sys.maxsize

    for i in range(0,len(a)):
        destructions=0
        for j in range(0,len(a)):
            if a[j]>=a[i]:
                destructions+=abs(a[i]-a[j])
            else:
                destructions+=a[j]
        if destructions<mini:
            mini=destructions
    return mini



a=[1,2,3,4]

print(solution(a))