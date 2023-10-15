# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # can store nodes in a hashmap/set, return if duplicate if found
        myset = set()
        while head:
            if head in myset:
                return True
            myset.add(head)
            head = head.next
        return False
