class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort()
            s = stones.pop()-stones.pop()
            if s>0:
                stones.append(s)

        return stones[0] if stones else 0
            