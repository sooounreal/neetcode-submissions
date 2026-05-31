class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(2*n)]

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[n+i] = nums[i]
        return ans