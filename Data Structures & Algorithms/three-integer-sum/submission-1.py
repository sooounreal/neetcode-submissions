class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            target = -nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    res.add((nums[i], nums[left], nums[right]))
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        r = [[a,b,c] for a,b,c in res]
        return r

