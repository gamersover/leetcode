from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        newHead = Node(head.val)
        curr, newCurr = head, newHead
        while curr.next:
            newCurr.next = Node(curr.next.val)
            newCurr.random = curr.next
            curr.next = newCurr
            curr = newCurr.random
            newCurr = newCurr.next

        curr.next = newCurr

        curr = head
        while curr and curr.next:
            nextCurr = curr.next.random
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None

            curr = nextCurr
        return newHead



node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

Solution().copyRandomList(node1)