class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strS = [0] * 26
        strT = [0] * 26

        for s1, t1 in zip(s, t):
            strS[ord(s1) - ord('a')] += 1
            strT[ord(t1) - ord('a')] += 1
        return strS == strT    