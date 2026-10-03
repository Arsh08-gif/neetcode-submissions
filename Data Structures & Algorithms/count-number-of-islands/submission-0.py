from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        count = 0
        q = []
        vis = [[False] * m for _ in range(n)] 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not vis[i][j]:
                    vis[i][j] = True
                    q.append((i,j))
                    while(q):
                        r,c = q.pop()

                        if c+1<m and grid[r][c+1] == "1" and not vis[r][c+1]:
                            vis[r][c+1] = True
                            q.append((r,c+1))
                        if r+1<n and grid[r+1][c] == "1" and not vis[r+1][c]:
                            vis[r+1][c] = True
                            q.append((r+1,c))
                        if c>0 and grid[r][c-1] == "1" and not vis[r][c-1]:
                            vis[r][c-1] = True
                            q.append((r,c-1))
                        if r>0 and grid[r-1][c] == "1" and not vis[r-1][c]:
                            vis[r-1][c] = True
                            q.append((r-1,c))
                    count += 1
                    print(count)
        return count

                        




        