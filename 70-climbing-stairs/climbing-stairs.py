class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        count = 3    
        x_2 = 2
        x_1 = 3

        for _ in range(3, n):
            count = x_1 + x_2
            x_2 = x_1
            x_1 = count
        return count    