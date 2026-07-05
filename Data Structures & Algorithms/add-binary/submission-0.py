class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            n = 0
            if i >= 0 :
                n += int(a[i])
            if j >= 0:
                n += int(b[j])
            n += carry
            carry = n //2
            res.append(str(n % 2))
            i -= 1
            j -= 1
        return ''.join(res[::-1])
