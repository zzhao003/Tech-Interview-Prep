class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)

        # MEMOIZATION

        # memo = {}
        # if n in memo:
        #     return memo[n]
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # memo[n] = self.fib(n-1) + self.fib(n-2)
        # return memo[n]
        
        # TABULATION
        if n == 0:
            return 0
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        print(arr)
        for i in range(n+1):
            if i+2 < n+1:
                arr[i+2] = arr[i] + arr[i+1]
        return arr[n]