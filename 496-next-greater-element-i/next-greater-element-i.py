class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        stack = []
        res = []

        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        for val in nums1:
            res.append(d.get(val, -1))
        return res    