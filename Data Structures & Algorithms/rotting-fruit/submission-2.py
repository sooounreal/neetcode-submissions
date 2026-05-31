class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        self.fresh_count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    self.fresh_count += 1
        
        if self.fresh_count == 0:
            return 0
        
        while True:
            # update grid
            has_changed = False
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 2:
                        if self.spread(grid, r,c):
                            has_changed = True
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            print(grid)
            if not has_changed:
                break
            res += 1
            if self.fresh_count == 0:
                return res
            
        
        return -1

    def spread(self, grid, r, c):
        has_changed = False
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for d in directions:
            dr, dc = d[0], d[1]
            if not (0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0])):
                continue
            if grid[r+dr][c+dc] != 1:
                continue
            grid[r+dr][c+dc] = 3
            self.fresh_count -= 1
            has_changed = True
        print("spread", has_changed)
        return has_changed


