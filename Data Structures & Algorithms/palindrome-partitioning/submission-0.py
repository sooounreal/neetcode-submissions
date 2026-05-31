class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []
        def dfs(l):
            if l == len(s):
                res.append(cur[:])
                return
            
            for r in range(l+1, len(s)+1):
                if s[l:r] == s[l:r][::-1]:
                    cur.append(s[l:r])
                    dfs(r)
                    cur.pop()
        
        dfs(0)
        return res