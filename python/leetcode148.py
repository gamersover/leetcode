from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        mid = self.find_middle(head)
        second = mid.next
        mid.next = None
        first = self.sortList(head)
        second = self.sortList(second)
        new_head = self.merge(first, second)
        return new_head


    def find_middle(self, head):
        fast, slow = head.next.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        fake_head = ListNode(0)
        curr = fake_head
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        if head1 is None:
            curr.next = head2
        else:
            curr.next = head1
        return fake_head.next



if __name__ == "__main__":
    node4 = ListNode(3)
    node3 = ListNode(1, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(4, node2)
    Solution().sortList(node1)