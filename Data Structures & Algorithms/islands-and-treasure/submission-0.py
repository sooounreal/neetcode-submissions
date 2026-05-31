class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    self.trav(grid, r-1, c, 1)
                    self.trav(grid, r+1, c, 1)
                    self.trav(grid, r, c-1, 1)
                    self.trav(grid, r, c+1, 1)
        


    def trav(self, grid, r, c, val):
        if r < 0 or r >= len(grid):
            return
        if c < 0 or c >= len(grid[0]):
            return
        
        if grid[r][c] == -1:
            return
        if grid[r][c] < val:
            return
        grid[r][c] = val
        self.trav(grid, r-1, c, val+1)
        self.trav(grid, r, c-1, val+1)
        self.trav(grid, r, c+1, val+1)
        self.trav(grid, r+1, c, val+1)