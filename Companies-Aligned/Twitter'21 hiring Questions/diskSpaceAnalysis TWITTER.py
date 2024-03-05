from collections import deque
def findMax(space, x):
    n = len(space)
    if n * x == 0:
        return []
    if x > n:
        return []

    deq = deque()
    res = []
    i = 0
    while i < n:
        if deq and deq[0] == i - x:
            deq.popleft()
        while deq and space[deq[-1]] > space[i]:
            deq.pop()
        deq.append(i)

        if i >= x - 1:
            res.append(space[deq[0]])
        i += 1
    return max(res)


if __name__ == '__main__':
    hdd = [62, 64, 77, 75, 71, 60, 79, 75]
    k =4
    findMax(hdd, k)
# nums=[1,2,3,1,2]
# k=1
# n=len(nums)
# print(printMax(nums,n,k))
