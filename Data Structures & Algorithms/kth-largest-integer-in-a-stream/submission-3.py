class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums) #convert array to a min heap
        while len(self.nums)>k:
            heapq.heappop(self.nums) #this is so that heap is k amount of elements initially already.

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
