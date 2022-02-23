def joshibkl(arr1,arr2):
    count = 0
    m = len(arr1)
    n = len(arr2)

    if m<n:
        for i in range(0,n):
            if arr2[i] not in arr1:
                count+=1
    else:
        for i in range(0,m):
            if arr1[i] not in arr2:
                count+=1

    return count



