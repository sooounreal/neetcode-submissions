class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        cur_max = 1
        left = 0
        right = 1
        cur_set = set(s[left])
        while left <= right and right < len(s):
            if s[right] not in cur_set:
                cur_set.add(s[right])
                cur_max = max(cur_max, right-left+1)
                right += 1
            else:
                cur_set.remove(s[left])
                left += 1
            # print(left,right,cur_set, cur_max)
        return cur_max
            