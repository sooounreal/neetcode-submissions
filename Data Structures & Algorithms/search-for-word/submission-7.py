class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        seen = set()
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
        def dfs(r, c, i):
            if word[i] != board[r][c]:
                return False
            if i == len(word) - 1:
                return True
            seen.add((r,c))
            for dx, dy in directions:
                x = r + dx
                y = c + dy
                if 0 <= x < m and 0 <= y < n and \
                    word[i+1] == board[x][y] and (x,y) not in seen:
                    if dfs(x, y, i+1):
                        return True
            seen.remove((r,c))
            return False

        
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True

        return False