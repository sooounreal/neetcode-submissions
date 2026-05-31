class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.is_pal(s,left) or self.is_pal(s,right)
            left += 1
            right -= 1
    
        return True


    def is_pal(self, s, i):
        left = 0 if i != 0 else 1
        right = len(s) - 1 if i < len(s) - 1 else len(s) - 2

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            if left == i:
                left += 1
            if right == i:
                right -= 1
        return True