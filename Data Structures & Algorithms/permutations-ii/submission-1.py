class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = [False for i in range(len(nums))]

        def dfs(cur, seen):
            # print(cur, seen)
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
         
            for i in range(len(seen)):
                if seen[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and seen[i-1]:
                    continue
                # add i
                cur.append(nums[i])
                seen[i] = True
                dfs(cur, seen)
                
                cur.pop()
                seen[i] = False
                
        dfs([],seen)
        return res
