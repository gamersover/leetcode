from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.pred = TreeNode(float("-inf"))

        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            if self.pred.val > root.val:
                if self.first is None:
                    self.first = self.pred
                self.second = root

            self.pred = root
            in_order(root.right)

        if root is None:
            return

        in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node3
node3.right = node2

Solution().recoverTree(node1)



