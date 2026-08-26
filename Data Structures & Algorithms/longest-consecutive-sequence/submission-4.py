class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        if len(nums)==0:
            return 0

        count = 1
        left = 0 
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] ==1:
                count+=1
            left+=1
            count = max(count, i - left +1)
            


        return count