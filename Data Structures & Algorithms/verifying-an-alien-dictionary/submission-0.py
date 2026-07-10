class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i in range(26):
            order_dict[order[i]] = i
        
        first_word = 0
        
        while first_word < len(words) - 1:
            left = words[first_word]
            right = words[first_word+1]
            
            for i in range(min(len(left), len(right))):
                if order_dict[left[i]] > order_dict[right[i]]:
                    return False
                elif order_dict[left[i]] < order_dict[right[i]]:
                    break
                elif i == len(right) - 1:
                    return False
            first_word += 1
        return True
            
            


