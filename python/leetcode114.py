from typing import Optional
from utils import TreeNode, build_tree


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left:
                left_last = root.left
                while left_last.right:
                    left_last = left_last.right
                left_last.right = root.right
                root.right = root.left
                root.left = None


root = build_tree([1, 2, 5, 3, 4, 6, 7, 8, None, 9, None, None, 11])
Solution().flatten(root)
