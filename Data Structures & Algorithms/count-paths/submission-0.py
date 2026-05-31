class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if dp[r][c]:
                    continue
                dp[r][c] = 0
                if r+1 < m:
                    dp[r][c] += dp[r+1][c]
                if c+1 < n:
                    if not dp[r][c+1]:
                        print(dp)
                        print(r,c)
                    dp[r][c] += dp[r][c+1]
        return dp[0][0]