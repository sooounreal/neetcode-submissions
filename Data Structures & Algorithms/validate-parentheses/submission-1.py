class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rev_map = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack or stack.pop() != rev_map[c]:
                    return False
        return len(stack) == 0
