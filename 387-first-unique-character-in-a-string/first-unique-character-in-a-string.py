class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for strs in s:
            d[strs] = d.get(strs, 0) + 1
        for i in range(len(s)):
            if d.get(s[i]) == 1:
                return i
        return -1        