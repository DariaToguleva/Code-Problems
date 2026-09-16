class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}

        for num in nums:
            if d.get(num, 0) > 0:
                d[num] -= 1
            else:
                d[num] = d.get(num, 0) + 1
        for num, c in d.items():
            if c == 1:
                return num