from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:

        steps = 0

        queue = deque([0])
        while queue:
            print(queue)
            next_right = 0
            for i in range(len(queue)):
                pos = queue.popleft()
                if pos == len(nums) - 1:
                    return steps
                next_right = max(next_right, pos+nums[pos])
            
            for j in range(pos+1, min(next_right+1, len(nums))):
                queue.append(j)
            steps += 1


