# # Built In Function
# array=[1,3,5,3,7,9,3]
# array.remove(3)
# print(array)


array=[1,5,3,7,3,9,3]

def removefirstoccurence(array,key):
    removed=0
    i=0
    while(array[i]!=key):
        i+=1
    array.pop(i)
    return array

print(removefirstoccurence(array,key=3))
