class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        used = [False for i in range(len(nums))]
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
           
            for j in range(len(nums)):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                used[j] = True
                cur.append(nums[j])
                dfs(cur)
                used[j] = False
                cur.pop()
        
        dfs([])
        return res
