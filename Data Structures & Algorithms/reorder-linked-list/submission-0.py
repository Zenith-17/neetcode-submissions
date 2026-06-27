# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        def llMid(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

     
        mid = llMid(head)

      
        second = reverseList(mid.next)
        mid.next = None

       
        first = head

        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2