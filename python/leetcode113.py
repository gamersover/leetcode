from typing import Optional, List
from utils import TreeNode, build_tree

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.all_path = []
        self.dfs(root, targetSum, [])
        return self.all_path

    def dfs(self, root, sum_, path):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None and sum_ == root.val:
            self.all_path.append(path[:])

        self.dfs(root.left, sum_ - root.val, path)
        self.dfs(root.right, sum_ - root.val, path)
        path.pop()



arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = build_tree(arr)

ans = Solution().pathSum(root, 22)
print(ans)
