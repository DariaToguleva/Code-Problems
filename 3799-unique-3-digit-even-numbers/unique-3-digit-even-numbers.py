class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()
        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                result.add(perm)
        return len(result)