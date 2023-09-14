class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash={}
        # for el in nums:
        #     hash[el] = 1 + hash.get(el, 0)
        # arr = hash.items()
        # print(arr)
        # sortArr = sorted(arr, key=lambda arr:arr[1],reverse=True)
        # return [sortArr[i][0] for i in range(k)]
        # O(n+nlogn)

        #method 2 with O(n) bucket sort
        hash={}
        freq = [[] for i in range(len(nums)+1)]
        # make a count hashmap
        for el in nums:
            hash[el] = 1 + hash.get(el, 0)
        #make an array with index = count 
        for key, value in hash.items():
            freq[value].append(key)
        #return k output
        res = []
        for i in range(len(freq)-1 , 0 , -1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    return res 

