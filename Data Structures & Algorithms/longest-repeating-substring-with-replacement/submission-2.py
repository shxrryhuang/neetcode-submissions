class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}

        left = 0
        maxFreq = 0
        res = 0
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0)+1
            maxFreq = max(maxFreq, hash[s[i]])
            while (i-left+1) - maxFreq > k:
                hash[s[left]] -=1
                left+=1
            res = max(res, i-left+1)
        return res
        