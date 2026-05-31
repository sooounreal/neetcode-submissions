class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cur = nums[0]

        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            cur = nums[i]
            if nums[cur-1] == cur:
                return cur
            nums[i], nums[cur-1] = nums[cur-1], cur

        