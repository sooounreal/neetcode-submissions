class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9
        for r in range(9):
            # check rows
            valid = [1 for _ in range(9)]
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if valid[int(v)-1] == 1:
                    valid[int(v)-1] = 0
                else:
                    return False
            
        
        for c in range(9):
            # check rows
            valid = [1 for _ in range(9)]
            for r in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if valid[int(v)-1] == 1:
                    valid[int(v)-1] = 0
                else:
                    return False
        
        for i in range(9):
            x = (i//3) * 3
            y = (i%3) * 3
            valid = [1 for _ in range(9)]
            for r in range(3):
                for c in range(3):
                    v = board[x+r][y+c]
                    if v == ".":
                        continue
                    
                    if valid[int(v)-1] == 1:
                        valid[int(v)-1] = 0
                    else:
                        return False
        return True


