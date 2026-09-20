class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        maxVol = 0

        while i < j:
            maxVol = max(maxVol, min(height[i], height[j]) * (j - i))
            if height[j] >= height[i]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
        return maxVol        