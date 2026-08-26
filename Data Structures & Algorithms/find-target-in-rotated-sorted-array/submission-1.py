class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left + right) //2

            if nums[mid]>nums[right]:
                left = mid + 1
            elif nums[mid] <nums[right]:
                right = mid
            elif nums[mid]==target:
                return mid
            else:
                return -1
        return -1
