from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    values = {}
    for idx, value in enumerate(nums):
        print("1 : "+str(idx),value)
        if target - value in values:
            print("2 : "+str(target-value),value)
            return [values[target - value], idx]
        else:
            values[value] = idx
            print("3 : "+str(values))

arr=[2,11,7,15]
target=9
print(twoSum(arr,target))



print(9//10)