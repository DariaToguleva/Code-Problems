class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for word in strs:
            arr = [0] * 26
            for i in range(len(word)):
                arr[ord(word[i]) - ord('a')] += 1
            key = tuple(arr)    
            if d.get(key):
                d[key].append(word)
            else:
                d[key] = [word]    
        return list(d.values())