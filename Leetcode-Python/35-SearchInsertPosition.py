class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n=len(nums)
        l=0
        h=n-1

        while (l<=h):
            m=(l+h)//2

            if nums[m]==target:
                return m
            elif (target > nums[m]):
                l = m+1
            elif (target < nums[m]):
                h = m-1
        return l