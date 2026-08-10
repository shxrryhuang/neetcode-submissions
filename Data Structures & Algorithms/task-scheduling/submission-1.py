class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1+ count.get(i,0)

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        queue = deque()

        while queue or maxHeap:
            time+=1
            if maxHeap:
                remaining = 1+heapq.heappop(maxHeap)
                if remaining < 0:
                    queue.append((remaining, time+n))
            
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time
