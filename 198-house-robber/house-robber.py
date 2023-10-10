class Solution:
    def rob(self, nums: List[int], memo = {}) -> int:
        # n = len(nums)
        # dp = [0]*(n+1)
        # dp[1] = nums[0]
        # for i in range(1, n):
        #     dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        # print(dp)
        # return dp[-1]
        if tuple(nums) in memo: return memo[tuple(nums)]
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
  
#   // recursive call
#   // case 1: take the first house and skip the second and run recursive calls on the remainding
        remaindingNums1 = nums[2:]
        takeFirst = nums[0] + self.rob(remaindingNums1)
#   // case 2: take the second house
        remaindingNums2 = nums[3:]
        takeSecond = nums[1] + self.rob(remaindingNums2)
        
        memo[tuple(nums)] = max(takeFirst, takeSecond)
        return memo[tuple(nums)]