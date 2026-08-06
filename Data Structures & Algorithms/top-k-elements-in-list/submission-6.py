class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1+ hash.get(nums[i],0)


        for num, count in hash.items():
            sort = sorted(hash.keys(), key = lambda x: hash[x], reverse = True)

        
        return sort[:k]