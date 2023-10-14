# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], pre = None) -> Optional[ListNode]:
        # pre = None
        # cur = head
        # while cur != None:
        #     nextNode = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nextNode
        # return pre

        # RECURSION
        # b.c 
        if head == None: return pre
        
        nextNode = head.next
        head.next = pre
        pre = head
        return self.reverseList(nextNode, pre)


