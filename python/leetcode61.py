from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        last_node = head
        num_nodes = 1
        while last_node.next != None:
            last_node = last_node.next
            num_nodes += 1

        last_node.next = head
        for _ in range(num_nodes- k % num_nodes):
            last_node = last_node.next

        head = last_node.next
        last_node.next = None
        return head
