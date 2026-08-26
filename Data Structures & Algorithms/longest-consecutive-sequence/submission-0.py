class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] ==1:
                count+=1
            


        return count