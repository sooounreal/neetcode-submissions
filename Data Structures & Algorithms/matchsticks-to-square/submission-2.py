class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        side_len = sum(matchsticks) / 4
        if max(matchsticks) > side_len:
            return False

        def dfs(used_sticks, n_left, rem_len):
            if rem_len == 0:
                if n_left == 0:
                    return True
                return dfs(used_sticks, n_left, side_len)

            for i in range(len(matchsticks)):
                if used_sticks[i] or matchsticks[i] > rem_len or matchsticks[i] > side_len:
                    continue
                # use current
                used_sticks[i] = True
                if dfs(used_sticks, n_left - 1, rem_len-matchsticks[i]):
                    return True
                used_sticks[i] = False
            return False
        
        return dfs([False for i in range(len(matchsticks))], len(matchsticks), side_len)

            