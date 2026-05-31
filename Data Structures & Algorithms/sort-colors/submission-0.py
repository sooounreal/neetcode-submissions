class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for n in nums:
            counts[n] += 1
        
        res = []
        cur = 0
        for i in range(len(nums)):
            while counts[cur] == 0:
                cur += 1
            nums[i] = cur
            counts[cur] -= 1
        