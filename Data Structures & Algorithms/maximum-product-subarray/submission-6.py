class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = 1
        dp_max = 1
        cur_max = int(-1e5)

        for n in nums:
            if n > 0:
                dp_max = dp_max * n
                dp_min = dp_min * n
            elif n == 0:
                cur_max = max(cur_max, n)
                dp_max = 1
                dp_min = 1
                continue
            else:
                dp_max, dp_min = dp_min * n, dp_max * n
            dp_max = max(n, dp_max)
            dp_min = min(n, dp_min)
            print(n, dp_max, dp_min)
            cur_max = max(cur_max, dp_max)
        return cur_max
