class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1+ hash.get(nums[i],0)

        freq = [[] for i in range(len(nums)+1)]
        for num, count in hash.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
