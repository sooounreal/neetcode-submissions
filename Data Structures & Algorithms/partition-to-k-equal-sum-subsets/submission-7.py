class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        
        used = [False for _ in range(len(nums))]
        cache = {}

        def dfs(mask, rem, num_left):
            if rem < 0:
                return False
            if mask in cache:
                return cache[mask]

            if rem == 0 and num_left == 1:
                cache[mask] = True
                return True
            
            if rem == 0:
                return dfs(mask, target, num_left-1)
            
            for i in range(len(nums)):
                if (mask >> i) & 1:
                    continue
                
                
                if dfs(mask | (1 << i), rem-nums[i], num_left):
                    cache[mask] = True
                    return True
            
            cache[mask] = False
            return False
        
        return dfs(0, target, k)

