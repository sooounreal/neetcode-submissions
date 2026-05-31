from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        queue = deque()
        seen = set()

        for n in nums:
            if len(queue) > k:
                p = queue.popleft()
                seen.remove(p)
            if n in seen:
                return True
            queue.append(n)
            seen.add(n)
        return False
