

def solution1(A):

    values = set(A)
    n = len(A)
    steps = 0
    final = n

    for i in range(n):
        count = 0
        visited = values.copy()
        for j in range(i, n):
            if (A[j] in visited):
                visited.remove(A[j])
            else:
                pass
            count = count + 1
            if (len(visited) == 0):
                if(count<final):
                    steps=count
                else:
                    steps=final

                final = steps
                break

    return steps
a=[7,5,2,7,2,7,4,7]
print(solution1(a))


def solution(A):
    n=len(A)
    if n==0 or n==1:
        return n

    start=0
    end=0
    visited=[False]*n
    visited[A[0]-1]=1

    for i in range(0,n):
        indec=A[i]-1
        visited[indec]+=1
        if(A[i]==A[i-1]):
            continue
        end=i

        while(visited[A[start]-1]>1):
            visited[A[start] - 1]-=1
            start+=1


    return end-start





a = [2,1,1,3,2,1,1,3]
print(solution(a))