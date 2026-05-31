class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = sum(weights)
        cur_sol = right

        while left <= right:
            mid = (left + right) // 2
            if self.can_ship(weights, days, mid):
                cur_sol = mid
                right = mid - 1
            else:
                left = mid + 1
        return cur_sol
    
    def can_ship(self, weights, max_days, cap):
        days = 1
        cur = cap
        for w in weights:
            if cap < w:
                return False
            if cur >= w:
                cur -= w
            else:
                cur = cap - w
                days += 1
        return days <= max_days
