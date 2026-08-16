from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
    
        memo = [-1]*len(nums) #initialize memo

        def dp(i):
            if i>=len(nums):
                return 0 
            if memo[i]!= -1: #if computed already, return memo
                return memo[i]
            memo[i]=max(dp(i+1),nums[i]+dp(i+2)) #else compute it
            return memo[i]
        return dp(0)

        