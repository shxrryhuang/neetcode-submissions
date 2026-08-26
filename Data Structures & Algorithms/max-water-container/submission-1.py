class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1
        maxArea = 0 
        currArea = 0

        for i in range(len(heights)):
            width = right - left 

            if currArea >= maxArea:
                maxArea = currArea
            
            if heights[left]>heights[right]:
                currArea = width*heights[right]
                right-=1

            if heights[left]<heights[right]:
                currArea = width*heights[left]
                left+=1
            
            if heights[left]==heights[right] and right!=left:
                currArea = width*heights[left]
            

        return maxArea