class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # r = w = b = 0
        # for num in nums:
        #     if num == 0:
        #         r += 1
        #     elif num == 1:
        #         w += 1
        #     elif num == 2:
        #         b += 1
        # for i in range(len(nums)):
        #     if r > 0:
        #         nums[i] = 0
        #         r -= 1
        #     elif w > 0:
        #         nums[i] = 1
        #         w -= 1
        #     elif b > 0:
        #         nums[i] = 2
        #         b -= 1

        l, r = 0, len(nums)-1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        