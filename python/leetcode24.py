class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        fakeHead = ListNode(0)
        fakeHead.next = head
        curr = fakeHead
        while curr.next and curr.next.next:
            first = curr.next
            second = first.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr = first
        return fakeHead.next