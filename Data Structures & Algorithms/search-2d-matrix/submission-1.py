class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bot = m - 1
        if matrix[0][0] > target:
            return False

        # binary search on col 0
        while top <= bot:
            r = (top+bot)//2
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] > target:
                bot = r - 1
            else:
                top = r + 1

        if matrix[r][0] > target:
            r -= 1
        print(r)
        # binary search on row r
        left = 0
        right = n - 1
        while left <= right:
            c = (left+right)//2
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = c - 1
            else:
                left = c + 1
        return False