class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for i in range(len(nums))]
        def dfs(i, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            if i == len(nums):
                return
            if used[i]:
                dfs(i+1, cur)
                return
            
            # use i next
            cur.append(nums[i])
            used[i] = True
            dfs(0, cur)
            cur.pop()
            used[i] = False
            # don't use i next
            dfs(i+1, cur)
        
        dfs(0, [])
        return res
            
