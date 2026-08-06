class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        
        if len(nums)==0:
            return 0 
        
        count = 1
        longest = 1
        for i in range(len(num)-1):
            if num[i+1]-num[i] == 1:
                count+=1
            else:
                count=1

            longest = max(longest,count)

        return longest