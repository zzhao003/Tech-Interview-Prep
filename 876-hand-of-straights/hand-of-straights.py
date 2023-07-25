# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize:
#             return False
#         # make a frequency hash
#         hashM = {}
#         for n in hand:
#             hashM[n] = 1 + hashM.get(n, 0)
#         #make a minHeap with the keys of hash
#         minH = list(hashM.keys())
#         heapq.heapify(minH)
#         #loop over each el in minHeap to see if their following els are consecutive
#         while minH:
#             first = minH[0]
#             #check the following el
#             for i in range(first, first + groupSize):
#                 #check if 1, 2, 3 are in hash, if not return False
#                 if i not in hashM:
#                     return False
#                 #decrement frequency of i in hashM
#                 hashM[i] -= 1
#                 if hashM[i] == 0:
#                     if i != minH[0]:
#                         return False
#                     heapq.heappop(minH)
#             return True
                
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

            