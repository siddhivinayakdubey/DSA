# # Built-In Function
# array=[1,3,5,3,7,9,3]
# key=3
# print(array.count(key))
#



# array=[1,3,5,3,7,9,3]
# n=len(array)
# count=0
# key=1
# # O(N)
# for i in range(n):
#     if array[i]==key:
#         count+=1
#
# print(count)


# From Counter
from collections import Counter

array=[1,3,5,3,7,9,3]
key=3
c=Counter(array)
print(c[key])