from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
          
            # Two choices at each house:
            # 1. Rob current house and skip next house (index + 2)
            # 2. Skip current house and move to next house (index + 1)
            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)
          
            # Return the maximum of both choices
            return max(rob_current, skip_current)
      
        # Start the recursion from house at index 0
        return dfs(0)

        
