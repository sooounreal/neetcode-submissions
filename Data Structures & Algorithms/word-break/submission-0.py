class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n:True}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                m = len(word)
                if len(word) > n - i or s[i:i+m] != word:
                    continue
                else:
                    if dfs(i+m):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        
        return dfs(0)

            
