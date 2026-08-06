class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1+ hash.get(nums[i],0)

        #after you count the items 
        # 1:1, 2:2:,3:3
        # you want to find a way to return the top k frequent elements
        #3,2 would be returned if k = 2


        
            sorted_nums = sorted(hash.keys(), key=lambda x: hash[x], reverse=True)
        return sorted_nums[:k]
        