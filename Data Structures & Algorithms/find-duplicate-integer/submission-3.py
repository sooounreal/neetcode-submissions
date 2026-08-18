class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            v = nums[i]-1
            if v == i:
                i += 1
            elif nums[i] == nums[v]:
                return v+1
            else:
                nums[i], nums[v] = nums[v], nums[i]
        