# def getSumAbsoluteDifferences(nums):
#     sum = 0
#     n = len(nums)
#     for i in range(0, n - 1):
#         for j in range(0, n - 1):
#             sum += abs(nums[i] - nums[j])
#             print(sum)
#         nums[i] = sum
#
#     return nums
#
# nums = [2,4,7]
# print(getSumAbsoluteDifferences(nums))

nums = [2,3,5]
temp=[]

n = len(nums)
l=0

for l in range(0,n):
    r = 0
    value = 0
    while (r < n ):
        value += abs(nums[l] - nums[r])
        r += 1
    temp.append(value)
    l += 1



print(temp)


# arr=[2,5,8,3,6,9]
#
# sum=arr[0]-arr[5]
# arr[0]=sum
# print(arr)