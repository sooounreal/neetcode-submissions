class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        used = [[False for _ in range(n)] for _ in range(m)]

        def dfs(r, c, cur_len):
            if cur_len == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if used[r][c] or board[r][c] != word[cur_len]:
                return False
            
            cur_len += 1
            used[r][c] = True
            # up
            if dfs(r-1, c, cur_len):
                return True

            # down
            if dfs(r+1, c, cur_len):
                return True

            # left
            if dfs(r, c-1, cur_len):
                return True

            # right
            if dfs(r, c+1, cur_len):
                return True
            
            cur_len -= 1
            used[r][c] = False
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r,c, 0):
                    return True
        return False