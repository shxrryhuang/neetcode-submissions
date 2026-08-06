class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hash = {}
        maxFreq = 0
        left = 0
        ans = 0
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0)+1
            maxFreq = max(maxFreq, hash[s[i]])

            while (i-left+1) - maxFreq >k:
                hash[s[left]]-=1
                left+=1
            ans = max(ans, i-left+1)


        return ans