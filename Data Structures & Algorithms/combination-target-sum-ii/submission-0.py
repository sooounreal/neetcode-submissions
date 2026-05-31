class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = sorted(candidates)
        res = []
        cur = []

        def dfs(i, rem):
            # print(i, rem, cur)
            if rem == 0:
                res.append(cur.copy())
                return
            if rem < 0 or i >= len(cand):
                return
            
            
            
            cur.append(cand[i])
            dfs(i+1, rem - cand[i])

            cur.pop()
            while i + 1 < len(cand) and cand[i] == cand[i+1]:
                i += 1
            dfs(i+1, rem)
        dfs(0, target)
        return res
        