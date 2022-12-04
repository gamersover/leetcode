# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_tree(arr):
    node_arr = []
    root_idx = 0
    left_child_idx = 1
    root = Node(arr[root_idx])
    node_arr.append(root)
    while root_idx < len(arr):
        if root is not None:
            if left_child_idx >= len(arr) or arr[left_child_idx] is None:
                root.left = None
            else:
                root.left = Node(arr[left_child_idx])
            node_arr.append(root.left)

            if left_child_idx+1 >= len(arr) or arr[left_child_idx+1] is None:
                root.right = None
            else:
                root.right = Node(arr[left_child_idx+1])
            node_arr.append(root.right)

            left_child_idx += 2

        root_idx += 1
        root = node_arr[root_idx]
    return node_arr[0]



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        if root.left and root.right:
            root.left.next = root.right
        if root.next:
            left_ = root.right if root.right else root.left
            node, right_ = root.next, None
            while node:
                if node.left:
                    right_ = node.left
                    break
                elif node.right:
                    right_ = node.right
                    break
                else:
                    node = node.next
            if left_ and right_:
                left_.next = right_
        self.connect(root.right)
        self.connect(root.left)
        return root



root = build_tree([2,1,3,0,7,9,1,2,None,1,0,None,None,8,8,None,None,None,None,7])
Solution().connect(root)