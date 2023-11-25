from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        curr = head
        while curr.next:
            prev = dummy
            while prev.next.val < curr.next.val:
                prev = prev.next
            if prev == curr:
                curr = curr.next
                continue
            node = curr.next
            curr.next = node.next
            node.next = prev.next
            prev.next = node
        return dummy.next
