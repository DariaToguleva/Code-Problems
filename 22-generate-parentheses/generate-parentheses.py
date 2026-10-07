class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def gen(now,open, close):
            if len(now) == n * 2:
                res.append(now)
                return
            if open < n:
                gen(now + "(", open + 1, close)
            if close < open:
                gen(now + ")", open, close + 1) 
        
        gen("", 0, 0)
        return res        