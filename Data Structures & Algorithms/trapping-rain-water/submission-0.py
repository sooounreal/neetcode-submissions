class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n
        for i in range(1, n):
            max_l[i] = max(max_l[i-1], height[i-1])
            max_r[n-1-i] = max(max_r[n-i], height[n-i])
        
        print(max_l)
        print(max_r)
        res = 0
        for i in range(n):
            res += max(min(max_l[i], max_r[i]) - height[i], 0)
        return res

