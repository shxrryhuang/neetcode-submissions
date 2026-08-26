class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        seen = set()
        left = 0

        for i in range(len(s)):
            if s[i] in seen:
                longest+=1
                longest = max(longest, i-left+1)

            if s[i] not in seen:
                seen.add(s[i])
                if k>0:
                    k-=1
        
        return longest