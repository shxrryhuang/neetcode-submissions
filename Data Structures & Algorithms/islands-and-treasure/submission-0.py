class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        row, col = len(grid),len(grid[0])
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==-1:
                    continue #mark as visited
                if grid[r][c]==0:
                    queue.append((r,c,0))

      
        while queue:
            for i in range(len(queue)):
                r,c,dist = queue.popleft()

                for dr,dc in directions:
                    nr,nc = dr+r, dc+c 

                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==2147483647:
                        grid[nr][nc]= dist+1
                        queue.append((nr,nc,dist+1))