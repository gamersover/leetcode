from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(next=head)
        pre = fakeHead
        curr = head
        cnt = 0
        while curr:
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
                cnt += 1
            if cnt > 0:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
            cnt = 0
        return fakeHead.next


