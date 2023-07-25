class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums)-1:
            furtherestJump = 0
            for i in range(l, r+1):
                furtherestJump = max(furtherestJump, i + nums[i])
            l = r+1
            r = furtherestJump
            res += 1
        return res
