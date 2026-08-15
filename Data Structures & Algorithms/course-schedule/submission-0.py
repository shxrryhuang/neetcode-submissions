class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]

        for x,y in prerequisites:
            graph[x].append(y)
        
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited: 
                return True

            visiting.add(node)
            for prereq in graph[node]:
                if not dfs(prereq):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
