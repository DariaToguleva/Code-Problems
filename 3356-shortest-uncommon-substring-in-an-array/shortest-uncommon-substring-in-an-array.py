class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        maps = {}
        for i in arr:
            visited = set()
            for j in range(len(i)):
                for k in range(j + 1, len(i) + 1):
                    visited.add(i[j : k])
            for vis in visited:
                maps[vis] = maps.get(vis, 0) + 1
        ans = []
        for s in arr:
            best = ""
            for length in range(1, len(s) + 1):
                cands = []
                for i in range(len(s) - length + 1):
                    temp = s[i : i + length]
                    if maps[temp] == 1:
                        cands.append(temp)
                if len(cands) >0:
                    best = cands[0]
                    for c in cands:
                        if c < best:
                            best = c
                    break
            ans.append(best)
        return ans