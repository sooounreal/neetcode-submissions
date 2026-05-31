class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,5,6,7, 9,10] 
        people.sort()
        res = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            rem = limit - people[right]
            right -= 1

            if rem >= people[left]:
                left += 1
            res += 1
        
        return res


