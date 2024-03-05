# array=[1,3,5,7,9]
# array.insert(2,4)
# print(array)

# Traditional Method

# def inserting(array,pos,value):
#     array.append(value)
#     print(array)
#     n=len(array)
#     for i in reversed(range(pos+1,n)):
#         temp=array[i]
#         array[i]=array[i-1]
#         array[i-1]=temp
#     return array
#
# array=[1,3,5,7,9]
# pos=2
# value=4
# print(array)
# print(inserting(array,pos,value))

# # Lesser Time Complexity
#
def inserting(array,pos,value):
    n=len(array)
    newarr=array[:pos]
    newarr.append(value)
    newarr=newarr+array[pos:]

    return newarr

array=[1,3,5,7,9]
pos=2
value=4
print(array)
print(inserting(array,pos,value))