class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        output = []

        q = []
        for i in range(m):
            q.append((i,0))
            pacific_visited.add((i,0))
        for j in range(1,n):
            q.append((0,j))
            pacific_visited.add((0,j))
        
        while q:
            r,c = q.pop()
            if r+1 < m and (r+1,c) not in pacific_visited and heights[r+1][c] >= heights[r][c]:
                q.append((r+1,c))
                pacific_visited.add((r+1,c))
            if c+1 < n and (r,c+1) not in pacific_visited and heights[r][c+1] >= heights[r][c]:
                q.append((r,c+1))   
                pacific_visited.add((r,c+1))
            if r-1 >= 0 and (r-1,c) not in pacific_visited and heights[r-1][c] >= heights[r][c]:
                q.append((r-1,c))
                pacific_visited.add((r-1,c))
            if c-1 >= 0 and (r,c-1) not in pacific_visited and heights[r][c-1] >= heights[r][c]:
                q.append((r,c-1))
                pacific_visited.add((r,c-1))

        for i in range(m-1,-1,-1):
            q.append((i,n-1))
            atlantic_visited.add((i,n-1))
        for j in range(n-1,-1,-1):
            q.append((m-1,j))
            atlantic_visited.add((m-1,j))

        
        while q:
            r,c = q.pop()
            if r+1 < m and (r+1,c) not in atlantic_visited and heights[r+1][c] >= heights[r][c]:
                q.append((r+1,c))
                atlantic_visited.add((r+1,c))
            if c+1 < n and (r,c+1) not in atlantic_visited and heights[r][c+1] >= heights[r][c]:
                q.append((r,c+1))   
                atlantic_visited.add((r,c+1))
            if r-1 >= 0 and (r-1,c) not in atlantic_visited and heights[r-1][c] >= heights[r][c]:
                q.append((r-1,c))
                atlantic_visited.add((r-1,c))
            if c-1 >= 0 and (r,c-1) not in atlantic_visited and heights[r][c-1] >= heights[r][c]:
                q.append((r,c-1))
                atlantic_visited.add((r,c-1))
            
        for cell in pacific_visited:
            r,c = cell
            if (r,c) in atlantic_visited:
                output.append([r,c])
        
        return output

                
        

            

                
        