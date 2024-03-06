class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum=float('-inf')
        currentSum=0

        for num in nums:
            currentSum+=num

            maxsum=max(currentSum,maxsum)

            if currentSum<0:
                currentSum=0

        return maxsum