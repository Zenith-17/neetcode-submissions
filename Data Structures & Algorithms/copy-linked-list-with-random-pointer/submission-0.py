class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}

        # Pass 1: create copies
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: connect next and random
        curr = head
        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next

        return mp[head]