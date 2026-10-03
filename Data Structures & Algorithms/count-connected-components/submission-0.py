class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for __ in range(n)]
        count = 0

        for edge in edges:
            a,b = edge
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def dfs(node):
            if not vis[node]: vis[node] = True
            for neigh in adj_list[node]:
                if not vis[neigh]:
                    dfs(neigh)
        
        vis = [False]*n
        for i in range(n):
            if not vis[i]:
                dfs(i)
                count += 1

        return count

        
        
        

        