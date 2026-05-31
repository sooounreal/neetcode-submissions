from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        if len(s) == 1:
            return True
        n = len(s)

        seen = set([0])
        queue = deque([0])
        while queue:
            pos = queue.popleft()
            for j in range(minJump, maxJump+1):
                if pos+j == n-1:
                    return True
                
                if (pos+j) not in seen:
                    seen.add(pos+j)
                    if pos+j < n and s[pos + j] == "0" :
                        queue.append(pos+j)
                        
        return False
                    
            



        