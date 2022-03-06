def solution(a,k):
    a.sort()
    n=len(a)
    return a[k-1]
a=[7,10,4,3,20,15]
k=3
print(solution(a,k))

