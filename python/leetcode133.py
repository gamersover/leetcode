# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def clone(self, node):
        if node is None:
            return None

        else:
            head = Node(node.val)
            self.all_nodes[node] = head
            for inode in node.neighbors:
                if inode in self.all_nodes:
                    head.neighbors.append(self.all_nodes[inode])
                else:
                    nei = self.clone(inode)
                    head.neighbors.append(nei)
            return head

    def cloneGraph(self, node: 'Node') -> 'Node':
        self.all_nodes = dict()
        return self.clone(node)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node4]
node4.neighbors = [node2, node3]

chead = Solution().cloneGraph(node1)