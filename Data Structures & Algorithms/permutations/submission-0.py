class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = []

        def dfs(i):
            print(i, used)
            
            if len(used) == len(nums):
                # print('got result', [nums[j] for j in used])
                res.append([nums[j] for j in used])
                return
            for k in range(len(nums)):
                if k not in used:
                    used.append(k)
                    dfs(k)
                    used.pop()

        dfs(0)
        return res
