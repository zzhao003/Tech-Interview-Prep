class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []: return [[]]
        res = []
        for num in nums:
            newlist = [x for x in nums if x != num]
            listOut = self.permute(newlist)
            for li in listOut:
                res.append(li +[num])


        return res
