class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        p1, p2 = head, head
        i = 0
        while i < n and p2 is not None:
            p2 = p2.next
            i += 1
        
        if p2 is None:
            head = p1.next
            return head
        
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next        
        p1.next = p1.next.next

        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    Solution().removeNthFromEnd(node1, 2)
