class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = strs[0]
        j = len(sub)
        for stri in strs:
            while stri[0 : j] != sub[0 : j]:
                j -= 1
                sub = sub[0 : j]
        return sub        