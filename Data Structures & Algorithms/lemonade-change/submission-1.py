class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if fives < 1:
                    return False
                if tens < 1 and fives < 3:
                    return False
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            print(b, fives, tens)
        return True
                