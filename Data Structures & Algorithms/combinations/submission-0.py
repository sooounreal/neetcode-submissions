class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i > n:
                return
            
            # add i
            cur.append(i)
            dfs(i+1, cur)
            # don't add i
            cur.pop()
            dfs(i+1, cur)
        
        dfs(1, [])
        return res