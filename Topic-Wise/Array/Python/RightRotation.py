# nums=[1,2,3,4,5,6,7]
# k=3
# n = len(nums)
# # def RightRotation(nums):
# #     for x in range(0, k):
# #         temp = nums[n - 1]
# #
# #         for i in reversed(range(0, n)):
# #             nums[i] = nums[i - 1];
# #             nums[0] = temp;
# #         temp=nums[n-1]
# #     return nums
# #
# # print(RightRotation(nums))
#
#
# for x in range(0, 1):
#     temp = nums[n - 1]
#     print(temp)
#     for i in reversed(range(n)):
#         print(i)
#         print(nums[i])
#         nums[i] = nums[i-1];
#
#
#
#     nums[0] = temp;
#     print(nums)
#     print(temp)
#
# n = len(nums)
# for x in range(0, k):
#     temp = nums[n - 1]
#
#     for i in reversed(range(n)):
#         nums[i] = nums[i - 1];
#     nums[0] = temp;
# return nums


nums=[1,2,3,4,5,6,7]
k=3
# def hello(nums,k):
#
#     n = len(nums)
#
#     q=k%n
#     sliced1=nums[-q:]
#     sliced2=nums[:n-q]
#     nums=sliced1+sliced2
#     return nums
#
# print(hello(nums,k))

n = len(nums)

temp= []
for i in range(0,n):
    temp.append(nums[(i+k+1)%n])

nums = temp
print(nums)
