class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                bitA = int(a[i])
            else:
                bitA = 0   
            if j >= 0:
                bitB = int(b[j])
            else:
                bitB = 0
            total = bitA + bitB + carry  
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return ''.join(reversed(result))     