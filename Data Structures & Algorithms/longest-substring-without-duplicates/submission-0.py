class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        if len(s) ==0:
            return 0
        currLength = 0
        maxLength = 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            if s[i] not in seen:
                seen.add(s[i])
                maxLength = max(maxLength,i-l+1)

        return maxLength