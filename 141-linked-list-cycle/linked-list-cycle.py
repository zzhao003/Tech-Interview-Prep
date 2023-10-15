# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store nodes in a hashmap/set, return if duplicate if found
        # myset = set()
        # while head:
        #     if head in myset:
        #         return True
        #     myset.add(head)
        #     head = head.next
        # return False

        # TWO POINTERS
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False