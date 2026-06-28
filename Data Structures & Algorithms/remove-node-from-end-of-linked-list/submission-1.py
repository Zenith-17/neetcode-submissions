# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def LLlen(head):
            t = head
            cl = 0
            while t:
                cl += 1
                t = t.next
            return cl

        cl = LLlen(head)

        if n == cl:
            return head.next

        t = head

        for _ in range(cl - n - 1):
            t = t.next

        t.next = t.next.next

        return head