class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        i, j = 0, 0
        arr = set()
        maxL = 0

        while j < len(s):
            while s[j] in arr:
                arr.remove(s[i])
                i += 1
            arr.add(s[j])   
            j += 1
            maxL = max(maxL, len(arr))
        return maxL    