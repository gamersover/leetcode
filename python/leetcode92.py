from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fakeHead = ListNode(0, head)
        i = 1
        pre = fakeHead
        curr = head
        while i < left:
            pre = curr
            curr = curr.next
            i += 1


        start = curr
        while i < right:
            nex = curr.next
            nnex = nex.next
            nex.next = start
            start = nex
            curr.next = nnex
            i += 1

        pre.next = start
        return fakeHead.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution().reverseBetween(node1, 1, 1)

