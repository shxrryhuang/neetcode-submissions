class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1
        maxArea = 0 
        currArea = 0

        for i in range(len(heights)):
            width = right - left

            if currArea >= maxArea:
                maxArea = currArea
            
            currArea = width * min(heights[left],heights[right])
            if heights[left]>heights[right]:
                right-=1

            if heights[left]<heights[right]:
                left+=1            

        return maxArea