from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    values = {}
    for i, v in enumerate(nums):
        if target - v in values:
            return [values[target - v], i]
        else:
            values[v] = i

arr=[2,11,7,15]
target=9
print(twoSum(arr,target))
