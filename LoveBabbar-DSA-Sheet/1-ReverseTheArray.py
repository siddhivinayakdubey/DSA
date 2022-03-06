def solution(array):
    array=[1,3,5,7,9,8]
    n=len(array)
    x=n-1
    for i in range(0,n//2):
        temp=array[i]
        array[i]=array[x]
        array[x]=temp
        x-=1
    return array


