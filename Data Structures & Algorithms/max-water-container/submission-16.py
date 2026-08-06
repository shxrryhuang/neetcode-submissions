class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1
        maxArea = 0 

        while left<right:
            width = right - left
            #currArea = width * min(heights[left],heights[right])
            
            if heights[left]>=heights[right]:
                currArea = width * heights[right]
                right-=1

            elif heights[left]<=heights[right]:
                currArea = width * heights[left]
                left+=1   

            
            maxArea = max(maxArea,currArea)
         

        return maxArea