class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j] represents number of operations to make word1[i:] to word2[j:]
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for col in range(n+1):
            dp[m][col] = n-col
        for row in range(m+1):
            dp[row][n] = m - row
        
        for i in range(m):
            for j in range(n):
                row = m - 1 - i
                col = n - 1 - j

                if word1[row] == word2[col]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = 1 + min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])
        return dp[0][0]
        
