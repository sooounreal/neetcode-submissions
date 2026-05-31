class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= target:
                while cur_sum >= target:
                    res = min(res, r-l+1)
                    cur_sum -= nums[l]
                    l += 1
                    
        return res