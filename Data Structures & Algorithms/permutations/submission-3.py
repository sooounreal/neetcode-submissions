class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = [False for i in range(len(nums))]
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                cur.append(nums[j])
                used[j] = True
                dfs(cur)
                cur.pop()
                used[j] = False
        
        dfs(cur)
        return res