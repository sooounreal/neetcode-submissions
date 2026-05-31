class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = [False for i in range(len(nums))]
        res = []
        
        def dfs(cur, seen):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if seen[i]:
                    continue
                cur.append(nums[i])
                seen[i] = True
                dfs(cur, seen)
                cur.pop()
                seen[i] = False
        dfs([], seen)
        return res
        
