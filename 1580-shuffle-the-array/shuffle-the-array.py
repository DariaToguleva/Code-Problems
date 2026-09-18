class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, k, j = 0, 0, n
        arr = [0] * len(nums)

        while j < len(nums):
            arr[k] = nums[i]
            k += 1
            arr[k] = nums[j]
            k += 1
            i += 1
            j += 1
        return arr    
