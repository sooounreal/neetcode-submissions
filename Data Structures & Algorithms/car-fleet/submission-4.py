class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for i in range(len(speed)):
            fleets.append((position[i],speed[i]))
        
        fleets.sort(key=lambda tup: tup[0])
        print(fleets)
        
        next_p, next_s = fleets.pop()
        next_t = (target-next_p)/next_s
        result = 1
        for p, s in fleets[::-1]:
            t = (target-p)/s
            if t > next_t:
                result += 1
            next_t = max(t,next_t)

        return result



