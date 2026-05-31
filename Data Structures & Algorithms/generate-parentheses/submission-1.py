class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, l_rem, r_rem):
            if l_rem == 0 and r_rem == 0:
                res.append(cur)
                return
            if l_rem > r_rem:
                return
            
            if l_rem > 0:
                cur += "("
                dfs(cur, l_rem-1, r_rem)
                cur = cur[:-1]
            if r_rem > 0:
                cur = cur + ")"
                dfs(cur, l_rem, r_rem-1)
        
        dfs("", n, n)
        return res
            
            