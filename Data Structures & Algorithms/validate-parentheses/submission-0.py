class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"{":"}","(":")", "[":"]"}
        stack = []

        for b in s:
            if b in bracket:
                stack.append(b)
            else:
                if not stack:
                    return False
                if bracket[stack.pop()] !=b:
                    return False
                
        return not stack