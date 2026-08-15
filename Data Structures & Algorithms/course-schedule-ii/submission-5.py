class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(numCourses)]

        for x,y in prerequisites:
            graph[x].append(y)

        visited = set()
        cycle = set()
        order = []
        def dfs(node):
            if node in visited:
                return True
            if node in cycle:
                return False

            cycle.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited.add(node)
            cycle.remove(node)
            order.append(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
