array=[1,3,5,1,3,7,9]
def removingduplicates(array):
    n=len(array)

    newarr=[]
    for i in range(0,n):
        if array[i] not in newarr:
            newarr.append(array[i])

    return newarr

print(removingduplicates(array))