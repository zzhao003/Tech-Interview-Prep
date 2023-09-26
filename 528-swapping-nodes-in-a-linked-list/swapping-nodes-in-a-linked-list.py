# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the length of the list
        n = 0
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            n += 1
            cur = cur.next
        # traverse the list and at k ans n-k location, modify value
        cur2 = head
        for i in range(n):
            if i == k-1:
                cur2.val = arr[n-k]
            elif i == n-k:
                cur2.val = arr[k-1]
            cur2 = cur2.next
        return head
        