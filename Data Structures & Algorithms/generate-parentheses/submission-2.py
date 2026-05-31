class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(cur, n_open, n_closed):
            if n_open == n and n_closed == n:
                res.append("".join(cur))
                return
            
            if n_open > n or n_closed > n:
                return

            if n_open == n_closed:
                cur.append("(")
                dfs(cur, n_open+1, n_closed)
                cur.pop()
            elif n_open > n_closed:
                cur.append("(")
                dfs(cur, n_open+1, n_closed)
                cur.pop()

                cur.append(")")
                dfs(cur,n_open, n_closed+1)
                cur.pop()
        
        dfs(cur, 0, 0)
        return res
