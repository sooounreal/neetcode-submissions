class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, rem):
            print(i, cur, rem)
            if rem == 0:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or rem < 0:
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, rem-candidates[i])
            cur.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, cur, rem)
        dfs(0, [], target)
        return res
