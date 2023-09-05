class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1, 1
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp 
        # return one
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        print(dp)
        return dp[-1]
