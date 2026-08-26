class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        seen = {}
        left = 0
        length = len(s1)

        for i in range(len(s1)):
            seen[s1[i]] = 1+ seen.get(s1[i],0)

        
        for i in range(len(s2)):
            if s2[i] not in seen:
                length+=1
            if s2[i] in seen:
                length-=1
            
        
        return length == len(s2)-len(s1) 

        