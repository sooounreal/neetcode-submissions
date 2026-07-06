class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # len1 is shorter word
        len1 = len(word1)
        len2 = len(word2)
        if len1 > len2:
            len1, len2 = len2, len1
            word1, word2 = word2, word1
        
        visited = {}
        def dfs(i, j):
            if (i,j) in visited:
                return visited[(i,j)]
            
            if j > len2:
                return
            if i == len1 and j == len2:
                visited[(i,j)] = 0
                return visited[(i,j)]

            
            if i == len1:
                visited[(i,j)] = 1 + dfs(i, j+1)
                return visited[(i,j)]

            if j == len2:
                visited[(i,j)] = 1 + dfs(i+1, j)
                return visited[(i,j)]

            if word1[i] == word2[j]:
                visited[(i,j)] = dfs(i+1, j+1)
                return visited[(i,j)]
            else:
                # insert
                ins = dfs(i, j+1)
                # replace
                rep = dfs(i+1, j+1)
                # delete
                dele = dfs(i+1, j)
                visited[(i,j)] = 1 + min(ins,rep,dele)
                return visited[(i,j)]
        return dfs(0,0)


