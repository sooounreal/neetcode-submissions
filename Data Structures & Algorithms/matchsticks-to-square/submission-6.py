class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        edge_len = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        used = [False for _ in range(len(matchsticks))]
        def dfs(rem_len, rem_edges):
            if rem_edges == 0:
                return True
            if rem_len == 0:
                return dfs(edge_len, rem_edges-1)
            
            for i in range(len(matchsticks)):
                if used[i]:
                    continue
                if matchsticks[i] > rem_len:
                    break
                
                used[i] = True
                if dfs(rem_len-matchsticks[i], rem_edges):
                    return True
                used[i] = False
            return False
        
        return dfs(edge_len, 4)
                