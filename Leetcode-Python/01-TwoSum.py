class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}

        for i,x in enumerate(nums):
            y= target - x

            if y in dict:
                return [dict[y],i]
            dict[x]=i