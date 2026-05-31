class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used = [[False for _ in range(n)] for _ in range(n)]
        res = []
        placed = ["."*n for _ in range(n)]

        def dfs(cur, placed):
            if placed == n:

                res.append(cur.copy())
                return
            
            for r in range(n):
                for c in range(n):
                    if used[r][c]:
                        continue
                    if placed == 3:
                        print("pre", used, cur)
                    removed = use(used, r, c)
                    cur[r] = "." * c + "Q" + "."*(n-1-c)
                    if placed == 3:
                        print("pos", used, cur)
                    dfs(cur, placed+1)
                    restore(used, removed)
                    cur[r] = "."*n
                if placed <= r:
                    return
        
        def use(used, r, c):
            removed = []
            # same row
            for col in range(n):
                if not used[r][col]:
                    removed.append((r,col))
                    used[r][col] = True
            
            # same col
            for row in range(n):
                if not used[row][c]:
                    removed.append((row,c))
                    used[row][c] = True

            # diag
            # top left 
            row = r
            col = c
            while 0 <= row and 0 <= col:
                if not used[row][col]:
                    removed.append((row,col))
                    used[row][col] = True
                row -= 1
                col -= 1

            # bot left
            row = r
            col = c
            while row < n and 0 <= col:
                if not used[row][col]:
                    removed.append((row,col))
                    used[row][col] = True
                row += 1
                col -= 1
            
            # top right
            row = r
            col = c
            while 0 <= row and col < n:
                if not used[row][col]:
                    removed.append((row,col))
                    used[row][col] = True
                row -= 1
                col += 1
            

            # bot right
            row = r
            col = c
            while row < n and col < n:
                if not used[row][col]:
                    removed.append((row,col))
                    used[row][col] = True
                row += 1
                col += 1
            # print(r,c)
            # print(removed)
            return removed

        def restore(used, removed):
            for r,c in removed:
                used[r][c] = False
        
        dfs(placed,0)
        print(len(res))
        return res