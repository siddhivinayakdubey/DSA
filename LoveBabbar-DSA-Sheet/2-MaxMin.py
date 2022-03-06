def getMinMax(a, n):
    maxi = float('-inf')
    mini = float('inf')

    for i in range(0, n):
        if a[i] > maxi:
            maxi = a[i]
        if a[i] < mini:
            mini = a[i]

    return mini, maxi