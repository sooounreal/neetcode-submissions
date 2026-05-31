class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def visit(r, c):
            if (r,c) in visited:
                return
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != "1":
                return
            print("adding", r, c)
            visited.add((r,c))
            visit(r-1, c)
            visit(r+1, c)
            visit(r, c-1)
            visit(r, c+1)
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    print(row, col)
                    res += 1
                    visit(row, col)
        return res