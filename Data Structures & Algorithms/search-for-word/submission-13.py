class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(row, col, i):
            if i == len(word) - 1 and word[i] == board[row][col]:
                return True
            
            if not (0 <= row < n_rows) or not (0 <= col < n_cols):
                return False
            
            if word[i] != board[row][col]:
                return False
            
            visited[row][col] = True
            print(word[i], row, col)
            for dx, dy in directions:
                r = row+dx
                c = col+dy
                if (0 <= r < n_rows) and (0 <= c < n_cols) and not visited[r][c]:
                    if dfs(r, c, i+1):
                        return True
            visited[row][col] = False
            return False
                

        for r in range(n_rows):
            for c in range(n_cols):
                if dfs(r,c, 0):
                    return True
        return False