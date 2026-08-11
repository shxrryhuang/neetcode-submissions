class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 0
        queue = deque()
        fresh = 0 

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c)) 

        while queue and fresh>0:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh -=1
                        queue.append((nr,nc))
            res+=1

        if fresh>0:
            return -1
        
        return res 