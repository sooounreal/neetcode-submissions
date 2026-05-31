class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i, visited):
            if i >= len(word):
                return True
            if row >= rows or row < 0:
                return False
            if col >= cols or col < 0:
                return False
            if (row,col) in visited:
                return False


            
            
            if board[row][col] == word[i]:
                visited.add((row,col))
                
                left = dfs(row, col-1, i+1, visited)
                right = dfs(row, col+1, i+1, visited)
                up = dfs(row-1, col, i+1, visited)
                down = dfs(row+1, col, i+1, visited)
                if left or right or up or down:
                    return True
                visited.remove((row,col))
            return False



        for r in range(rows):
            for c in range(cols):
                visited = set()
                if dfs(r, c, 0, visited):
                    return True
        return False

    