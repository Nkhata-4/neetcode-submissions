class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        p = 1
        y = 1
        while y < n:
            ans = x + p
            x = p 
            p = ans
            y += 1
        
        if n == 1 or n == 0:
            ans = 1
        return ans



