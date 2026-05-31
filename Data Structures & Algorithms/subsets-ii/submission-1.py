class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []

        nums.sort()

        def dfs(i, cur):
            res.append(cur.copy())

            j = i
            while j < len(nums):
                cur.append(nums[j])
                dfs(j+1, cur)
                cur.pop()
                j += 1
                while j < len(nums) and nums[j-1] == nums[j]:
                    j += 1
        dfs(0, cur)
        return res
