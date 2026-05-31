class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_dict = {}
        
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1
        

        for left in range(len(s2)):
            s2_dict = {}
            right = left
            while right < len(s2):
                # total len = right - left + 1
                c = s2[right]
                s2_dict[c] = s2_dict.get(c, 0) + 1
                if s2_dict[c] <= s1_dict.get(c,0):
                    right += 1
                else:
                    break
                if right - left == len(s1):
                    print(left, right, s2_dict)
                    return True
            
        return False
# abdbac
# abc