import sys
def solution(a,d):
    final=[]
    mini=sys.maxsize
    final.append(min(a))
    for ele in a:
        if ele%10<mini:
            mini=ele%10
    y=[mini]*(d-1)
    final=final+y
    return final

a=[991,881]
d=3
print(solution(a,d))