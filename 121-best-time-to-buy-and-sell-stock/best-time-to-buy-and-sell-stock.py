class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # res = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         res = max(res, profit)
        #     else:
        #         l = r
        #     r += 1
        # return res
        # l = 0
        # res = 0
        # for r in range(len(prices)):
        #     profit = prices[r]- prices[l]
        #     if profit < 0:
        #         l = r
        #     res = max(res, profit)
        # return res
      l = 0 
      r = 1 
      
      # compare nums[l] and nums[r]
      # initialize a currMax variable
      currMax = 0
      
      while r < len(prices):
        if prices[l] > prices[r]: 
          l = r
          r += 1
        else: 
          localDifference = prices[r] - prices[l]
          currMax = max(currMax,localDifference)
          r += 1
          
      return currMax