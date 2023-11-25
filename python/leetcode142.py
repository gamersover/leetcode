from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return None

        meet_node = self.getMeetNode(head)

        if meet_node:
            entry = head
            while entry != meet_node:
                entry = entry.next
                meet_node = meet_node.next
            return entry
        else:
            return None

    def getMeetNode(self, head):
        fast, slow = head.next.next, head.next
        while fast is not None and fast.next is not None:
            if fast == slow:
                return slow
            else:
                fast = fast.next.next
                slow = slow.next
        return None



node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

Solution().detectCycle(node1)