class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)-1, -1, -1):
            longest = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, dp[j])
            dp[i] = longest + 1
        
        return max(dp)