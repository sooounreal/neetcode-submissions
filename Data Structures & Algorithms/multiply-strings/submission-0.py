class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #   123
        #    56
        #   6*3*10**0 + 6*2*10**1 + 6*1*10**2 + 5*3*10**1 + 5*2*10**2 + 

        if num1 == "0" or num2 == "0":
            return "0"
        
        res = 0
        for i in range(len(num1)):
            d1 = int(num1[-(i+1)])
            for j in range(len(num2)):
                d2 = int(num2[-(j+1)])
                res += d1*d2*10**(i+j)
        return str(res)
