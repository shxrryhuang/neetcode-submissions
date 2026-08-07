class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(path):
            if len(path)==len(nums):
                res.append(path.copy())
                
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack(path)
                path.pop()
            

        backtrack([])
        return res