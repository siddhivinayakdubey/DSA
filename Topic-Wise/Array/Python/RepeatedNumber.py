
# from collections import Counter
#
# A=[3,4,1,4,1]
# x = Counter(A)
# print(x)
#
# new_list = list([item for item in x if x[item] ==1])
# print(len(new_list))

from collections import Counter



    # @param A : tuple of integers
    # @return an integer
def repeatedNumber(A):
    x = Counter(A)
    y = list([item for item in x if x[item] == 1])
    count=len(y)

    return count
A=[3,4,1,4,1]
print(repeatedNumber(A))
