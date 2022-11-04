from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n+1)

    def generate(self, start, end):
        if start == end:
            return [None]
        if start == end - 1:
            return [TreeNode(start)]
        ans = []
        for i in range(start, end):
            left_trees = self.generate(start, i)
            right_trees = self.generate(i+1, end)
            for l in left_trees:
                for r in right_trees:
                    head = TreeNode(i)
                    head.left = l
                    head.right = r
                    ans.append(head)
        return ans



print(Solution().generateTrees(3))



