class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1, 1
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp 
        # return one
        # dp = [1]*(n+1)
        # for i in range(1,n):
        #     dp[i+1] = dp[i-1] + dp[i]
        # return dp[-1]


        # TABULATION
        table = [0] * (n+1)
        table[0] = 1
        table[1] = 1
        for i in range(2, n+1):
            table[i] = table[i-1] + table[i-2]

        return table[n]
