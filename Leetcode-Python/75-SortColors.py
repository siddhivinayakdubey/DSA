# Via HEAP

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = nums[:]
        heapq.heapify(h)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(h)



# Dutch National Flag algorithm

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i=0
        m=0
        j=len(nums)-1

        while(m<=j):
            if nums[m]==0:
                nums[i],nums[m]=nums[m],nums[i]
                i+=1
                m+=1
            
            elif nums[m]==1:
                m+=1

            elif nums[m]==2:
                nums[j],nums[m]=nums[m],nums[j]
                j-=1





            