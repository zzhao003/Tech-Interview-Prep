class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre = [1]
        # post = [1]
        # n = len(nums)
        # for i in range(n-1):
        #     pre.append(nums[i]*pre[i])
        #     post.append(nums[n-1-i]*post[i])
        # print(pre)
        # print(post)
        # return [pre[j]*post[n-1-j] for j in range(n)]
        pre, post = [1], [1]
        n = len(nums)
        for i in range(len(nums)-1):
            pre.append(pre[i]*nums[i])
            post.append(post[i]*nums[n-i-1])
        return [pre[j]*post[n-1-j] for j in range(n)]
