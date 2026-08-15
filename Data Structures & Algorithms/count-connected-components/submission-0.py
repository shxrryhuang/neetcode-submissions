class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0 
        
        res = 0
        graph = [[] for i in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1

        return res