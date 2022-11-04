from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        len_ = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
            len_ += 1

        left = self.buildTree(preorder[1:1+len_], inorder[:len_])
        right = self.buildTree(preorder[1+len_:], inorder[1+len_:])
        return TreeNode(preorder[0], left, right)


print(Solution().buildTree([1, 2], [2, 1]))