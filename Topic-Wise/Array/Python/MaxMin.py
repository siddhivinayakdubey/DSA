def MaxMin(arr):
    arr=sorted(arr)
    n=len(arr)
    sum=arr[0]+arr[n-1]
    return sum

arr=[-2, 1, -4, 5, 3]
# MaxMin(arr)
print(MaxMin(arr))