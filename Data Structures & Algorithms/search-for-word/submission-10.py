class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(r, c, i, visited):
            
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            if word[i] != board[r][c]:
                return False
            visited[(r,c)] = 0
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for direction in directions:
                dr, dc = direction
                if 0 <= r+dr < n_rows and 0 <= c+dc < n_cols and (r+dr, c+dc) not in visited:
                    if dfs(r+dr,c+dc, i+1, visited):
                        return True
            visited.pop((r,c))
            return False
            


        for r in range(n_rows):
            for c in range(n_cols):
                if dfs(r, c, 0, {}):
                    return True
        return False

