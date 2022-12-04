from typing import Optional
from utils import TreeNode, build_tree


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.get_max_sum(root)
        return self.max_sum

    def get_max_sum(self, root):
        if root is None:
            return 0

        left_max = max(self.get_max_sum(root.left), 0)
        right_max = max(self.get_max_sum(root.right), 0)
        root_tail_max = root.val + max(left_max, right_max)
        self.max_sum = max(root.val + left_max + right_max, self.max_sum)
        return root_tail_max
