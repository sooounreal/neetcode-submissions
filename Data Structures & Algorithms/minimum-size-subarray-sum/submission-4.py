class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            if total >= target:
                res = min(res, right-left+1)
                while total >= target:
                    
                    res = min(res, right-left+1)
                    #print(nums[left:right+1], total, res)
                    total -= nums[left]
                    left += 1
        if res > len(nums):
            return 0
        return res


