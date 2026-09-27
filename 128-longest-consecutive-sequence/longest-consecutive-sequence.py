class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums2 = set(nums)
        maxi = 0
        for num in nums2:
            count = 0
            if num - 1 in nums2:
                pass
            else:
                i = 1
                while num + i in nums2:
                    count+=1
                    i += 1
                maxi = max(count, maxi)
        return maxi + 1