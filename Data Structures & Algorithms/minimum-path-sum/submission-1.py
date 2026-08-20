class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[None for _ in range(n)] for _ in range(m)]
        # create boundaries
        dp[-1][-1] = grid[-1][-1]

        # [1,2,3]
        # [4,5,6]
        for row in range(m-2, -1, -1):
            print(row, dp)
            dp[row][-1] = dp[row+1][-1] + grid[row][-1]

        for col in range(n-2, -1, -1):
            dp[-1][col] = dp[-1][col+1] + grid[-1][col]
        
        print(dp)

        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
        
        return dp[0][0]