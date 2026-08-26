class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x**+y**2,x,y) for x,y in points]

        heapq.heapify(heap)

        res = []

        for i in range(k):
            dist,x,y = heapq.heappop(heap)

            res.append([x,y])

        return res