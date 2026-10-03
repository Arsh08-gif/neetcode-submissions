class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 --> 1
        # 1 ---> 0
        if not prerequisites :
            return True
        
        adjList = [[] for _ in range(numCourses)]
        for item in prerequisites:
            a,b = item
            adjList[a].append(b)
        
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visited:
                return True # explored and safe
            if course in visiting:
                return False # cycle detected
            
            visiting.add(course)
            for neighbor in adjList[course]:
                if not dfs(neighbor): return False

            visiting.remove(course) # acting like stack pop
            visited.add(course) # stack push

            return True
        
        for node in range(numCourses):
            if not dfs(node): return False
        return True





        




        