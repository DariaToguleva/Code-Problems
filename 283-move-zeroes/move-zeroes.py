class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       i, j = 0, 1

       while j < len(nums) and i < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
        j += 1    
        while i < len(nums) and nums[i] != 0:
            i += 1
            j = i + 1
        print(i, j)    