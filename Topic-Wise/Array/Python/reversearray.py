# Using Built-in Function
# array=[1,3,5,7,9]
# array.reverse()
# print(array)




# Reversing in O(n)

# array=[1,3,5,7,9]
# n=len(array)
# revarr=[]
# n=len(array)
# for i in reversed(range(0,n)):
#     revarr.append(array[i])
# print(revarr)


# Best speed algorithm

array=[1,3,5,7,9,8]
n=len(array)
x=n-1
for i in range(0,n//2):
    temp=array[i]
    array[i]=array[x]
    array[x]=temp
    x-=1
print(array)



