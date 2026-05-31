class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, seen):
            print(cur, seen)
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                cur.append(nums[i])
                seen.add(i)
                dfs(cur, seen)
                cur.pop()
                seen.remove(i)

        dfs([], set())
        return res