# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.find_middle_node(head)
        head2 = mid.next
        mid.next = None
        head2 = self.reverse_list(head2)
        self.merge_list(head, head2)

    def find_middle_node(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        curr = head
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = head
            head = temp
        return head

    def merge_list(self, head1, head2):
        while head1 and head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

Solution().reorderList(node1)