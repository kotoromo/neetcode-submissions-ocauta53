class Solution:
    def __init__(self):
        self.cache = dict()

    def climbStairs(self, n: int) -> int:
        if n in (0, 1): return 1
        elif n in self.cache: return self.cache[n]
        else: 
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.cache[n]