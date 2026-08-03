class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        even = total / k
        self.res = total
        n = len(nums)

        def find_opt_split(i, splits, cumsum, cur_max):
            if cumsum > self.res:
                return
            if i == n:
                self.res = min(self.res, cur_max)
                return
            if splits == 0:
                cur_max = max(cur_max, sum(nums[i:]))
                self.res = min(self.res, cur_max)
                return
            
            if cumsum + nums[i] <= max(even, cur_max):
                # dont split
                find_opt_split(i+1, splits, cumsum+nums[i], max(cur_max, cumsum+nums[i]))
            else:
                print(i, "else")
                # dont split
                find_opt_split(i+1, splits, cumsum+nums[i], max(cur_max, cumsum+nums[i]))
                # split
                find_opt_split(i, splits-1, 0, cur_max)

        find_opt_split(0, k-1, 0, 0)
        return self.res
