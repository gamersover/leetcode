from typing import Optional
from utils import TreeNode, build_tree


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pre_sum):
            if root is None:
                return 0
            sum_ = pre_sum * 10 + root.val
            if root.left is None and root.right is None:
                return sum_

            return dfs(root.left, sum_) + dfs(root.right, sum_)

        return dfs(root, 0)


root = build_tree([4, 9, 0, 5, 1])
print(Solution().sumNumbers(root))