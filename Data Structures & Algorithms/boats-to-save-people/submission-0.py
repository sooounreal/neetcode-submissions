class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people) - 1
        left = 0
        res = 0
        while left < right:
            if people[left] + people[right] <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                res += 1
                right -= 1
        if left == right:
            res += 1
        return res
    
    # [1,2,2,3,3]