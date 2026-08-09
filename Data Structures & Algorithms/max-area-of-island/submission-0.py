class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        row, col = len(grid),len(grid[0])
        res = 0

        if not grid:
            return 0 

        def dfs(r,c):
            if (0>r or 0>c or r>=row or c>=col or grid[r][c]==0):
                return 0 
            
            area = 1
            grid[r][c]=0
            for dr,dc in directions:
                area +=dfs(r+dr,c+dc)

            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    res = max(res,area)

        return res
                