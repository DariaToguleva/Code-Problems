class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxW = 0

        for i in range(len(accounts)):
            sums = 0
            for j in range(len(accounts[i])):
                sums += accounts[i][j]
            maxW = max(maxW, sums)
        return maxW    