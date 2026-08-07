class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path,opn,close):
            if len(path)==n*2:
                res.append("".join(path))
                return
            
            if opn<n:
                path.append("(")
                backtrack(path,opn+1,close)
                path.pop()
            if close<opn:
                path.append(")")
                backtrack(path,opn,close+1)
                path.pop()


        backtrack([],0,0)
        return res