class Solution:
    def trap(self, height: List[int]) -> int:

        left_h = [0 for _ in range(len(height))]
        right_h = [0 for _ in range(len(height))]


        cur_max = 0
        for i in range(1,len(height)):
            cur_max = max(height[i-1], cur_max)
            left_h[i] = cur_max

        cur_max = 0
        for i in range(len(height)-2, -1, -1):
            cur_max = max(height[i+1], cur_max)
            right_h[i] = cur_max
        
        print(left_h, right_h)
        res = 0
        for i in range(len(height)):
            res += max(min(left_h[i], right_h[i]) - height[i], 0)
        return res