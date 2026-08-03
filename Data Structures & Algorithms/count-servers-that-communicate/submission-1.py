class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                self.find_comm(grid, r, c, m, n)
        return self.res

    def find_comm(self, grid, r, c, m, n):
        
        found = False
        for i in range(m):
            if i == r:
                continue
            if grid[i][c] != 0:
                if grid[i][c] == 1:
                    self.res += 1
                    grid[i][c] = 2
                found = True
            
        for j in range(n):
            if j == c:
                continue
            if grid[r][j] != 0:
                if grid[r][j] == 1:
                    self.res += 1
                    grid[r][j] = 2
                found = True
            
        if found:
            grid[r][c] = 2
            self.res += 1
        print(r,c, self.res)
