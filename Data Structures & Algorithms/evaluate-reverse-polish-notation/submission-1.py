class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stack.append(int(t))
            else:
                second = stack.pop()   # popped SECOND operand (it was pushed last)
                first = stack.pop()    # popped FIRST operand (it was pushed first)

                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(int(first / second))  # truncate toward zero

        return stack[0]