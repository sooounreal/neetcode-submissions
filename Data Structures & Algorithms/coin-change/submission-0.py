class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = {}
        for c in coins:
            dp[c] = 1
        
        def change(x):
            if x == 0:
                return 0
            if x in dp:
                return dp[x]

            res = 1e9
            for c in coins:
                if x >= c:
                    rem = change(x-c)
                    res = min(1 + rem, res)

            dp[x] = res            
            return res

        r = change(amount)
        if r == 1e9:
            return -1
        return r

