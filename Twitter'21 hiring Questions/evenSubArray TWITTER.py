def distinct_subarrays(numbers, K):
    final_result = 0
    length = len(numbers)
    for i in range(length):
        array = []
        index = 0
        st = set()

        for j in range(i, length):
            if i == 0:
                if numbers[j] % 2 == 1:
                    array.append(1)
                else:
                    array.append(0)
                if array[index] <= K and numbers[j] not in st:
                    final_result += 1
                    st.add(numbers[j])
            else:
                if numbers[j] % 2 == 1:
                    array.append(temp[index] + 1)
                else:
                    array.append(temp[index])
                if array[index] <= K and tuple(numbers[index:j + 1]) not in st:
                    final_result += 1
                    st.add(tuple(numbers[index:j + 1]))
            index += 1
        temp = list(array)
    return final_result












#### MAIN CODE Time: O(N^2)
# def distinct_subarrays(nums, K):
#     ans = 0
#     n = len(nums)
#     for i in range(n):
#         temp2 = []
#         k = 0
#         check = set()
#         for j in range(i, n):
#             if i == 0:
#                 if nums[j] % 2 == 1:
#                     temp2.append(1)
#                 else:
#                     temp2.append(0)
#                 if temp2[k] <= K and nums[j] not in check:
#                     ans += 1
#                     check.add(nums[j])
#             else:
#                 if nums[j] % 2 == 1:
#                     temp2.append(temp1[k] + 1)
#                 else:
#                     temp2.append(temp1[k])
#                 if temp2[k] <= K and tuple(nums[k:j + 1]) not in check:
#                     ans += 1
#                     check.add(tuple(nums[k:j + 1]))
#             k += 1
#         temp1 = list(temp2)
#
#     return ans

nums=[3,2,3]
k=1
print(distinct_subarrays(nums,k))
