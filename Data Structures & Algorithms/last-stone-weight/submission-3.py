class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]

        heapq.heapify(heap)
        res = 0
        while len(heap)>1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            res = first - second

            heapq.heappush(heap,res)
        
        
        return -heap[0]