class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        def dfs(i, rem):
            if rem == 0:
                res.append(cur.copy())
                return
            if i == len(candidates):
                return
            if candidates[i] > rem:
                return
            
            # include
            cur.append(candidates[i])
            dfs(i+1, rem-candidates[i])
            cur.pop()
            # don't include
            i += 1
            while i < len(candidates) and candidates[i-1] == candidates[i]:
                i += 1
            dfs(i, rem)
            return
        
        dfs(0, target)
        return res