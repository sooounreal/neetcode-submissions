class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        if i < len(word1):
            for k in range(i, len(word1)):
                res.append(word1[k])
        
        if j < len(word2):
            for k in range(j, len(word2)):
                res.append(word2[k])
        return "".join(res)