class Solution:
    def fib(self, n: int, memo={}) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)

        # memoiozation
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]
        