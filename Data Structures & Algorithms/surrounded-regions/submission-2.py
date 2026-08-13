class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        row, col = len(board),len(board[0])
        queue = deque()

        for r in range(row):
            for c in range(col):
                if (r==0 or c==0 or r == row - 1 or c == col -1) and board[r][c] =="O":
                    queue.append((r,c))
                    board[r][c] ="S"

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr,nc = dr+r, dc+c

                    if 0<=nr<row and 0<=nc<col and board[nr][nc]=="O":
                        board[nr][nc] = "S"
                        queue.append((nr,nc))

        for r in range(row):
            for c in range(col):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="S":
                    board[r][c]="O"
                