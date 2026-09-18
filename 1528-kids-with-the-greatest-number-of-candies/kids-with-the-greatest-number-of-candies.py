class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        arr = [0] * len(candies)
        res = [False] * len(candies)
        maxC = 0

        for i in range(len(candies)):
            maxC = max(candies[i], maxC)
            arr[i] = candies[i] + extraCandies
        for i in range(len(candies)):
            if arr[i] >= maxC:
                res[i] = True
        return res        