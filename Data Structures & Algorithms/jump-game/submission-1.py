class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can = [False for _ in range(len(nums))]
        can[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i]+1):
                if i+j < len(nums) and can[i+j]:
                    can[i] = True
        print(can)
        return can[0]
