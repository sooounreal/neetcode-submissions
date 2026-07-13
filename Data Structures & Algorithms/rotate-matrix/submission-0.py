class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (i,j) -> (j,n-1-i)
        #   [a,b,c,d],
        #   [e,f,g,h],
        #   [i,j,k,l],
        #   [m,n,o,p],
        n = len(matrix)
        def rotate_outer(r1, c1, r2, c2):
            if r1 == r2 and c1 == c2:
                return
            if r1 > r2 and c1 > c2:
                return
            size = r2 - r1
            r = r1
            c = c1
            tmp = matrix[r][c]
            for i in range(size):
                for j in range(4):
                    matrix[c][n-1-r], tmp = tmp, matrix[c][n-1-r]
                    r, c = c, n-1-r
                c = c+1
                tmp = matrix[r][c]    
            rotate_outer(r1+1,c1+1, r2-1, c2-1)
        
        rotate_outer(0,0,n-1,n-1)
        return
        



