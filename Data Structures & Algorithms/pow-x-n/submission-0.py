class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        cache = {0:1, 1:x}

        def pow(n):
            if n < 0:
                return 1/pow(-n)
            if n in cache:
                return cache[n]
            
            half = n//2
            remainder = n - half
            cache[n] = pow(half) * pow(remainder)
            return cache[n]
        return pow(n)


        
