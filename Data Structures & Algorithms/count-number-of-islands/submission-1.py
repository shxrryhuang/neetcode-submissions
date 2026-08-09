class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid),len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        res = 0

        if not grid:
            return 0

        def dfs(r,c):
            if (r>=row or r<0 or c<0 or c>=col or grid[r][c]=="0" or (r,c) in visited):
                return
                        
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] =="1" and (r,c) not in visited:
                    dfs(r,c)
                    res +=1
        
        return res