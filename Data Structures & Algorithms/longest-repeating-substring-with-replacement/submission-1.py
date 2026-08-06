class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}

        l = 0
        maxFreq = 0
        res = 0
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0)+1
            maxFreq = max(maxFreq, hash[s[i]])
            while (i-l+1) - maxFreq > k:
                hash[s[l]] -=1
                l+=1
            res = max(res, i-l+1)
        return res
        