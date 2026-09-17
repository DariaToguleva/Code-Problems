class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rands = [0] * 26
        magaz = [0] * 26

        for l in ransomNote:
            rands[ord(l) - ord('a')] += 1
        for s in magazine:
            magaz[ord(s) - ord('a')] += 1
        if len(rands) > len(magaz):
            return False
        for i in range(len(rands)):
            if magaz[i] < rands[i]:
                return False
        return True        