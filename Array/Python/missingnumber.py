# Between 1 to 10
array=[1,2,3,4,6,7,8,9,10]
def missingnumber(array):
    n=len(array)
    numbercount=10
    missing=[]

    count=1
    for i in range(0,n):
        if array[i]!=count:
            missing.append(count)
            count+=1

    return missing

print(missingnumber(array))
