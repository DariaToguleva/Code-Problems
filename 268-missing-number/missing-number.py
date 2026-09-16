class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        arr = [-1] * (len(nums) + 1)
        for num in nums:
            arr[num] = num
        for i in range(len(arr)):
            if arr[i] == -1:
                return i