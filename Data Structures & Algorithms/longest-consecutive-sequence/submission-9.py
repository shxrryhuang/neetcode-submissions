class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        
        if len(nums)==0:
            return 0

        count = 1
        longest = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] ==1:
                count+=1
        
            else:
                count = 1
            
            longest = max(longest, count)

        return longest