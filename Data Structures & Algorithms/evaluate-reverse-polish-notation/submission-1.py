class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t not in "+-*/":
                stack.append(int(t))
            elif t == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif t == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif t == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            
        return stack[0]


