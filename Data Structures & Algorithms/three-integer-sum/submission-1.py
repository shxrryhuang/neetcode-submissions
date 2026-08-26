class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0 
        right = len(nums)-1
        i=1
        hash = {}
        nums.sort()
        res = []


        while left<right:
            if nums[left]+nums[right]+nums[i]>0:
                right-=1
            elif nums[left]+nums[right]+nums[i]<0:
                left+=1
                i+=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
        return res