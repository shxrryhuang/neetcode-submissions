class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1
        maxArea = 0 

        while left<right:
            width = right - left
            currArea = width * min(heights[left],heights[right])
            maxArea = max(currArea, maxArea)
            
            if heights[left]>=heights[right]:
                right-=1

            elif heights[left]<=heights[right]:
                left+=1            

        return maxArea