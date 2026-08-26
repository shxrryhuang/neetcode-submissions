class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                first = stack.pop()
                second = stack.pop()
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(second - first)
                    continue
                elif t == "*":
                    stack.append(first *second)
                elif t == "/":
                    stack.append(int(first/second))


        return stack[0]
