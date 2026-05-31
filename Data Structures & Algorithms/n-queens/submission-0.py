class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = ["."*n for i in range(n)]
        
        def dfs(r, queens, cur_board):
            if queens == n:
                res.append(cur.copy())
                return
            if r == n:
                return
            for c in range(n):
                if self.can_place(cur, r, c):
                    cur[r] = '.'*c + 'Q' + '.'*(n-c-1)
                    dfs(r+1, queens+1, cur)
                    cur[r] = '.'*n
        
        dfs(0, 0, cur)
        return res
    
    def can_place(self, cur, r, c):
        # loop over all Q's
        for row in range(len(cur)):
            for col in range(len(cur)):
                if cur[row][col] == 'Q':
                    if r == row or col == c or abs(row - r) == abs(col - c):
                        return False
        return True
