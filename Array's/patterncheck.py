array1=["red","green","green"]
array2=["a","b","b"]

def patterncheck(array):
    n=len(array)
    check=[]
    pattern=[]
    for i in range(0,n):
        if array[i] not in check:
            check.append(array[i])
            m=len(check)
            pattern.append(m-1)
        else:
            v=len(check)
            for j in range(0,v):
                if array[i]==check[j]:
                    pattern.append(j)
    return pattern

def matchit(array1, array2):
    patter1=patterncheck(array1)
    patter2=patterncheck(array2)

    if patter1==patter2:
        return True
    return False

print(matchit(array1,array2))