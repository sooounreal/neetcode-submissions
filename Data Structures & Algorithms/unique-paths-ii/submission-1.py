class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ways = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[m-1][n-1] == 0:
            ways[m-1][n-1] = 1

        # right col
        for r in range(m-2, -1, -1):
            if obstacleGrid[r][n-1] == 0:
                ways[r][n-1] = ways[r+1][n-1]

        # bot row
        for c in range(n-2, -1, -1):
            if obstacleGrid[m-1][c] == 0:
                ways[m-1][c] = ways[m-1][c+1]

        print(ways)
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if obstacleGrid[r][c] == 0:
                    ways[r][c] = ways[r+1][c] + ways[r][c+1]
        
        print(ways)
        return ways[0][0]

