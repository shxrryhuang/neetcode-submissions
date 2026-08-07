class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        def isPalindrome(string):
            left, right = 0, len(string)-1
            while left<right:
                if string[left]!=string[right]:
                    return False
                left+=1
                right-=1
            return True

        def backtrack(path,start):

            if start == len(s):
                res.append(path.copy())
                return 

            for i in range(start,len(s)):
                substring = s[start:i+1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(path,i+1)
                    path.pop()

        backtrack([],0)
        return res