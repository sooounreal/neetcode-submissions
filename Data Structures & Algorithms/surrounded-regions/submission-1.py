class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        def is_surrounded(r, c, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 'X' or (r,c) in visited:
                return True
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                return False
            visited.add((r,c))
            up = is_surrounded(r-1,c,visited)
            down = is_surrounded(r+1,c,visited)
            left = is_surrounded(r,c-1,visited)
            right = is_surrounded(r,c+1,visited)
            return up and down and left and right
        
        need_to_change = set()
        for r in range(rows):
            for c in range(cols):
                visited = set()
                if is_surrounded(r, c, visited):
                    print(r,c)
                    need_to_change = need_to_change.union(visited)
        
        for r,c in need_to_change:
            board[r][c] = 'X'
        