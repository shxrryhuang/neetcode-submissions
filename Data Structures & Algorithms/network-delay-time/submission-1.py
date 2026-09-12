class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #directed
        #minimum time for all n nodes
        #non-negative weights
        #acyclic

        #dikstra's algo 

        #1,2,3,4 = 3
        #1,4 = 4 (X)
        #u->v, t = weight

        #create directed graph
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))

        #Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

        '''
        adj = {1: [(2,1), (4,4)],
        2: [(3,1)],
        3: [(4,1)]}
       '''

        visit = set()
        time = 0 
        minHeap = [(0,k)] #time = 0, start = k

        while minHeap:
            currTime, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            visit.add(node)
            time = currTime

            for nextNode,weight in adj[node]:
                if nextNode not in visit:
                    heapq.heappush(minHeap,(currTime+weight,nextNode))
        
        return time if len(visit)==n else -1

        
