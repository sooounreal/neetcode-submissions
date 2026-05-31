class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# [1, 6, 3, 4, 5]
# [1, 2, 2, 3, 4]


# [2, 7, 1, 3, 4]
# [1, 2, 1, ]