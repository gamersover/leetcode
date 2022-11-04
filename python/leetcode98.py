import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, -math.inf, math.inf)

    def is_valid(self, root, lower, upper):
        if root is None:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        if not self.is_valid(root.left, lower, root.val):
            return False
        if not self.is_valid(root.right, root.val, upper):
            return False
        return True