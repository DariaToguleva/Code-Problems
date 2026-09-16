class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num1 = None
        count = 0

        for num in nums:
            if count == 0:
                num1 = num
            if num == num1:
                count += 1
            else:
                count -= 1
        return num1        