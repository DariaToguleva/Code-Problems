class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapH = {}

        for indx, num in enumerate(nums):
            if target - num in mapH:
                return [indx, mapH[target - num]]
            mapH[num] = indx   