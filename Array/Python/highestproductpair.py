# Traditional Method
# def pairs(array):
#     maxproduct=0
#     n=len(array)
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             product=array[i]*array[j]
#
#             if product>maxproduct:
#                 maxproduct=product
#                 maxnum1=array[i]
#                 maxnum2=array[j]
#     return maxnum1,maxnum2
#
# array=[0,-1,-2,-4,5,0,-6]
# print(pairs(array))


# Faster Method
array=[0,-1,-2,-4,5,0,-6]

def pair(array):
    array.sort()
    n=len(array)
    product1=array[0]*array[1]
    product2=array[n-1]*array[n-2]

    if product1>product2:
        return array[0],array[1]
    else:
        return array[n-1],array[n-2]

print(pair(array))

