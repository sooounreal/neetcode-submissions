class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        cur_max = 0
        while left < right:
            h = min(heights[left], heights[right])
            cur_max = max(cur_max, (right - left) * h)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return cur_max