import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        plist = []
        # 由于headq不能自定义比较器，所以需要一个序号i，在结点的val相同时，比较序号来排序
        i = 0
        for node in lists:
            if node is not None:
                heapq.heappush(plist, (node.val, i, node))
                i += 1
        
        fhead = ListNode()
        curr = fhead
        while len(plist) > 0:
            node = heapq.heappop(plist)[2]
            curr.next = node
            curr = curr.next

            if node.next is not None:
                heapq.heappush(plist, (node.next.val, i, node.next))
                i += 1
        
        return fhead.next
