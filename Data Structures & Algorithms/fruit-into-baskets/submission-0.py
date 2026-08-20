class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        fruit_count = {}
        res = 0

        while right < len(fruits):
            fruit_count[fruits[right]] = fruit_count.get(fruits[right],0) + 1
            if len(fruit_count.keys()) <= 2:
                res = max(res, right - left + 1)
            else:
                while len(fruit_count.keys()) > 2:
                    fruit_count[fruits[left]] -= 1
                    if fruit_count[fruits[left]] == 0:
                        fruit_count.pop(fruits[left])
                    left += 1
            right += 1
        return res