class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()
        def visit(r, c):
            # print("visit 1", r,c)
            if (r, c) in visited:
                return 0
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1:
                return 0
            
            visited.add((r,c))
            left = visit(r, c-1)
            up = visit(r-1, c)
            down = visit(r+1, c)
            right = visit(r, c+1)
            # print("visit", r, c, left, up, down,right)
            return 1 + left + up + down + right

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    # print(row, col)
                    res = max(res, visit(row, col))
        return res
                