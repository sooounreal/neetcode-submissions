class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack:
                prev_i, prev_t = stack[-1]
                if t > prev_t:
                    result[prev_i] = i - prev_i
                    stack.pop()
                else:
                    break
            stack.append((i,t))
        return result

# Input: temperatures = [30,38,30,36,35,40,28]
# stack = [(30,0),]
# Output: [1,4,1,2,1,0,0]
