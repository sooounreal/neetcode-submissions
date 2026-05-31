class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        used = [False for i in range(len(nums))]
        def dfs(i, cur):
            if len(cur) == len(nums)-1:
                cur.append(nums[i])
                res.append(cur.copy())
                cur.pop()
                return

            if i > len(nums):
                return
            
            cur.append(nums[i])
            used[i] = True
            for j in range(len(nums)):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue

                dfs(j, cur)
            used[i] = False
            cur.pop()
        
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                continue
            dfs(j, [])
        return res
