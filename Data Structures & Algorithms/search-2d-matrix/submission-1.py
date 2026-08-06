class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, (len(matrix)*len(matrix[0]))-1

        while left<= right:
            mid = (left+right) //2
            #find mid in 2d terms
            row, col = mid//len(matrix[0]), mid % len(matrix[0])

            if target>matrix[row][col]:
                left = mid + 1
            elif target<matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False