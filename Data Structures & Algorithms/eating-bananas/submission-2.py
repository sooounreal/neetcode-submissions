import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 100000000000
        while left <= right:
            m = (left+right) // 2
            cur_h = hours(m, piles)
            print(m,cur_h)
            if cur_h <= h:
                res = min(res, m)
                print("res", m, cur_h)
                right = m - 1
            else:
                left = m + 1
        return res

def hours(m, piles):
    h = 0
    for p in piles:
        h += max(math.ceil(p / m), 1)
    return h