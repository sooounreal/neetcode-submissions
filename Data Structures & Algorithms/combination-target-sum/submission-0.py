class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, rem):
            if rem < 0 or i >= len(nums):
                return
            if rem == 0:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i, rem-nums[i])
            cur.pop()
            dfs(i+1, rem)
        
        dfs(0, target)
        return res
