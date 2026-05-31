class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows = len(heights)
        n_cols = len(heights[0])

        can_pacific = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        can_atlantic = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        
        visited_p = set()
        visited_a = set()
        def pacific(i, j):
            if (i,j) in visited_p:
                return can_pacific[i][j]
            if i == 0 or j == 0:
                can_pacific[i][j] = 1
                return 1
            elif i < 0 or i >= n_rows or j < 0 or j >= n_cols:
                return -1
            elif can_pacific[i][j] == -1:
                return -1
            
            visited_p.add((i,j))
            # up
            if i > 0 and heights[i][j] >= heights[i-1][j] and pacific(i-1,j) == 1:
                can_pacific[i][j] = 1
                return 1
            # left
            if j > 0 and heights[i][j] >= heights[i][j-1] and pacific(i,j-1) == 1:
                can_pacific[i][j] = 1
                return 1
            # down
            if i < n_rows-1 and heights[i][j] >= heights[i+1][j] and pacific(i+1,j) == 1:
                can_pacific[i][j] = 1
                return 1
            
            # right
            if j < n_cols-1 and heights[i][j] >= heights[i][j+1] and pacific(i,j+1) == 1:
                can_pacific[i][j] = 1
                return 1
            return -1

        def atlantic(i, j):
            if (i,j) in visited_a:
                return can_atlantic[i][j]
            if i == n_rows-1 or j == n_cols-1:
                can_atlantic[i][j] = 1
                return 1
            elif i < 0 or i >= n_rows or j < 0 or j >= n_cols:
                return -1
            elif can_atlantic[i][j] == -1:
                return -1
            
            visited_a.add((i,j))
            # up
            if i > 0 and heights[i][j] >= heights[i-1][j] and atlantic(i-1,j) == 1:
                can_atlantic[i][j] = 1
                return 1
            # left
            if j > 0 and heights[i][j] >= heights[i][j-1] and atlantic(i,j-1) == 1:
                can_atlantic[i][j] = 1
                return 1
            # down
            if i < n_rows-1 and heights[i][j] >= heights[i+1][j] and atlantic(i+1,j) == 1:
                can_atlantic[i][j] = 1
                return 1
            
            # right
            if j < n_cols-1 and heights[i][j] >= heights[i][j+1] and atlantic(i,j+1) == 1:
                can_atlantic[i][j] = 1
                return 1
            return -1

        res = []
        for r in range(n_rows):
            for c in range(n_cols):
                p = pacific(r,c)
                a = atlantic(r,c)
                if p == 1 and a == 1:
                    res.append([r,c])
        return res