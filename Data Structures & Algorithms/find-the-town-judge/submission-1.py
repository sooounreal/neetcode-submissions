class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        trusted_by = {}
        for pair in trust:
            a, b = pair[0], pair[1]

            trusts[a] = trusts.get(a,[]) + [b]
            trusted_by[b] = trusted_by.get(b, []) + [a]
        
        
        for i in range(1, n+1):
            if i in trusts or i not in trusted_by:
                continue
            if len(trusted_by[i]) == n-1:
                return i
        return -1