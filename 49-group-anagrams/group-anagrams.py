class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}
        for s in strs:
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] += 1
            key = tuple(arr)
            if key not in words:
                words[key] = []
            words[key].append(s)
        return list(words.values())       