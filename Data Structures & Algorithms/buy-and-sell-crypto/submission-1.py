class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_on_day = []

        res = 0
        cur_min = 100
        for i in range(len(prices)):
            p = prices[i]
            res = max(res,  p - cur_min)
            cur_min = min(cur_min, p)
        
        return res

        

