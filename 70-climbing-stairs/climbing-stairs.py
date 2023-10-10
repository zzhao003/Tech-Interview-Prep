class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # TABULATION
        # table = [0] * (n+1)
        # table[0] = 1
        # table[1] = 1
        # for i in range(2, n+1):
        #     table[i] = table[i-1] + table[i-2]

        # return table[n]
        # MEMOIZATION
        if n in memo: return memo[n]
        if n == 1: return 1
        if n == 0: return 1
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return memo[n]


