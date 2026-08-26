class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(numCourses)]

        for x,y in prerequisites:
            graph[x].append(y)

        visited = set()
        order = []
        def dfs(node):
            if node in visited:
                return False
            if graph[node]==[]:
                order.append(node)
                return True

            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited.remove(node)
            graph[node]=[]
            order.append(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
