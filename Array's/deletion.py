def deletion(array,index):

    # Traditional Method

    # n=len(array)
    # for i in range(index,n-1):
    #     array[i]=array[i+1]
    # return array


    # Better Approch
    newarray=array[:index]
    newarray=newarray+array[index+1:]
    return newarray

array=[1,3,5,7,9]
index=2
print(deletion(array,index))


