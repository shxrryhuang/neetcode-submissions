class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seenS1= {}
        
        for i in range(len(s1)):
            if i in seenS1:
                seenS1[s1[i]] = 1 + seenS1.get(s1[i], 0)
            seenS1.add(s1[i])

        for i in range(len(s2)):
            if s2[i] in seenS1:
                seenS1[s2[i]] = seenS1.get(s2[i], 0) - 1

        