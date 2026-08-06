class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = (set(nums))
        
        if len(nums)==0:
            return 0 
        
        count = 1
        longest = 1
        for i in num:
            if i-1 not in num:
                count=1
                while i + count in num:
                    count+=1

            longest = max(longest,count)

        return longest