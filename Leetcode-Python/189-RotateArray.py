class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k>n:
            x=k%n
        else:
            x=k
        nums[:] = nums[n-x:]+nums[:n-x]