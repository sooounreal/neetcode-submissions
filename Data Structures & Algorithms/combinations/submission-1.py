class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        cur = []
        def dfs(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i > n:
                return
            
            # include
            cur.append(i)
            dfs(i+1)
            cur.pop()

            dfs(i+1)
        dfs(1)
        return res