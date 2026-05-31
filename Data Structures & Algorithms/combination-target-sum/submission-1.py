class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def dfs(i, rem):
            if rem == 0:
                res.append(cur.copy())
                return
            if i == len(nums):
                return
            if nums[i] > rem:
                return
            
            cur.append(nums[i])
            dfs(i, rem-nums[i])
            cur.pop()
            # don't include
            dfs(i+1, rem)
            return
        
        dfs(0, target)
        return res
            