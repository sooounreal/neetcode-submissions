class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            s_dict[c] = s_dict.get(c,0) + 1
        
        for c in t:
            t_dict[c] = t_dict.get(c,0) + 1
        
        keys = set(s_dict.keys()).union(set(t_dict.keys()))
        for k in keys:
            if k not in s_dict or k not in t_dict or s_dict[k] != t_dict[k]:
                return False
            
        return True