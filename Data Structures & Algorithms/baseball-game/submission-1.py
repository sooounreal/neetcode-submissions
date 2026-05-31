class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                left = stack[-1]
                right = stack[-2]
                stack.append(left+right)
            elif o == "D":
                left = stack[-1]
                stack.append(left * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        
        return sum(stack)