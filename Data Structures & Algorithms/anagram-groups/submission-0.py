class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            char_dict = {}
            for c in s:
                if c in char_dict:
                    char_dict[c] += 1
                else:
                    char_dict[c] = 1
            
            key = ""
            for k in sorted(char_dict.keys()):
                key += k
                key += str(char_dict[k])
            
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return res.values()