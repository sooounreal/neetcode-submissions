class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i, total):
            if total == 0:
                return True
            if i >= len(nums):
                return False
            if total < 0:
                return False
            
            return dfs(i+1, total-nums[i]) or dfs(i+1, total)
        
        return dfs(0, target)