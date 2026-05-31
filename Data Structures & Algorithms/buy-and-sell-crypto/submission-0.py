class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_list = [0 for i in range(len(prices))]
        cur_max = 0
        for i,p in enumerate(prices[::-1]):
            max_list[-(i+1)] = max(cur_max, p)
            cur_max = max(p, cur_max)
        
        print(max_list)
        res = 0
        for i,p in enumerate(prices):
            res = max(res, max_list[i]-p)
        return res

