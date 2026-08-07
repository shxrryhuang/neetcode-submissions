class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hmap = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        if digits == "":
            return []
        res = []
        def backtrack(path,start):
            if start == len(digits):
                res.append("".join(path))
                return

            c = hmap[digits[start]]
            for i in c:
                path.append(i)
                backtrack(path,start+1)
                path.pop()

        backtrack([],0)
        return res