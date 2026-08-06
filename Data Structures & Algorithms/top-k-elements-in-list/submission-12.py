class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1+ hash.get(nums[i],0)

        heap = []
        for i in hash.keys():
            heapq.heappush(heap,(hash[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res