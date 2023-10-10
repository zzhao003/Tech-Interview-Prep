
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP array with all elements initialized to 1
        dp = [[1] * m for _ in range(n)]

        # Iterate through the grid to calculate unique paths
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the number of unique paths from top-left to bottom-right
        return dp[n - 1][m - 1]