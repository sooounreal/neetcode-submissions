class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        cache = {}
        cur_total = 0
        for r in range(m):
            cur_total += matrix[r][0]
            cache[(r,0)] = cur_total

        cur_total = 0
        for c in range(n):
            cur_total += matrix[0][c]
            cache[(0,c)] = cur_total
        
        for r in range(1, m):
            for c in range(1, n):
                cache[(r,c)] = matrix[r][c] + cache[(r-1,c)] + cache[(r,c-1)] - cache[(r-1,c-1)]
        self.cache = cache

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full = self.cache[(row2, col2)]
        top_left = self.cache[(row1-1, col1-1)] if (row1 >= 1 and col1 >= 1) else 0
        top_right = self.cache[(row1-1, col2)] if row1 >= 1 else 0
        bot_left = self.cache[(row2, col1-1)] if col1 >= 1 else 0
        print(full, top_left, top_right, bot_left)
        return full + top_left - top_right - bot_left


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)