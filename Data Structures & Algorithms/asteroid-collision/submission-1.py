class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
                continue
            
            # stack exists and ast < 0
            while stack and ast < 0:
                prev = stack.pop()
                if prev < 0:
                    stack.append(prev)
                    break
                else:
                    if prev + ast == 0:
                        ast = 0
                        break
                    elif ast + prev > 0:
                        ast = prev
            if ast != 0:
                stack.append(ast)

        return stack


            
