from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 0:
                    if i > 0 and grid[i-1][j] > 0:
                        grid[i-1][j] = 1
                        q.append([i-1, j])
                    if j > 0 and grid[i][j-1] > 0:
                        grid[i][j-1] = 1
                        q.append([i, j-1])
                    if i+1 < len(grid) and grid[i+1][j] > 0:
                        grid[i+1][j] = 1
                        q.append([i+1, j])
                    if j+1 < len(grid[0]) and grid[i][j+1] > 0:
                        grid[i][j+1] = 1
                        q.append([i, j+1])
                    
                    while q:
                        r,c = q.popleft()
                        if r > 0 and grid[r-1][c] > 0:
                            if grid[r-1][c] > grid[r][c]+1:
                                grid[r-1][c] = grid[r][c] + 1
                                q.append([r-1,c])
                        if c > 0 and grid[r][c-1] > 0:
                            if grid[r][c-1] > grid[r][c] + 1:
                                grid[r][c-1] = grid[r][c] + 1
                                q.append([r,c-1])
                        if r+1 < len(grid) and grid[r+1][c] > 0:
                            if grid[r+1][c] > grid[r][c] + 1:
                                grid[r+1][c] = grid[r][c] + 1
                                q.append([r+1,c]) 
                        if c+1 < len(grid[0]) and grid[r][c+1] > 0:
                            if grid[r][c+1] > grid[r][c] + 1:
                                grid[r][c+1] = grid[r][c] + 1
                                q.append([r,c+1]) 
                    

        