class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path,start,total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(start,len(nums)):
                if total+nums[i]>target:
                    return
                path.append(nums[i])
                backtrack(path,i,total+nums[i])
                path.pop()

        backtrack([],0,0)
        return res