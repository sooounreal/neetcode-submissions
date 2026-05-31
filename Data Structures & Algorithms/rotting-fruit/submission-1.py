class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def rot(r, c):
            if r < 0 or r >= m:
                return 0
            if c < 0 or c >= n:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 3
                return 1
            return 0


        count = None
        minutes = -1
        while count is None or count > 0:
            count = 0
            print('start')
            has_fresh = False
            minutes += 1
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 2:
                        # print("rotting ", r,c)
                        count += rot(r-1, c) + rot(r+1, c) + rot(r, c+1) + rot(r, c-1)
                    elif grid[r][c] == 1:
                        has_fresh = True
            
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
        print(count)
        if has_fresh:
            return -1
        elif count == 0:
            return minutes
        else:
            return 0
        
        