class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}

        for c in chars:
            char_count[c] = char_count.get(c,0) + 1
        
        res = 0
        for w in words:
            word_char_count = {}
            covered = True
            for c in w:
                word_char_count[c] = word_char_count.get(c,0) + 1
                if c not in char_count or char_count[c] < word_char_count[c]:
                    covered = False
                    break
            if covered:
                res += len(w)
        return res