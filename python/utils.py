class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr):
    node_arr = []
    root_idx = 0
    left_child_idx = 1
    root = TreeNode(arr[root_idx])
    node_arr.append(root)
    while root_idx < len(arr):
        if root is not None:
            if left_child_idx >= len(arr) or arr[left_child_idx] is None:
                root.left = None
            else:
                root.left = TreeNode(arr[left_child_idx])
            node_arr.append(root.left)

            if left_child_idx+1 >= len(arr) or arr[left_child_idx+1] is None:
                root.right = None
            else:
                root.right = TreeNode(arr[left_child_idx+1])
            node_arr.append(root.right)

            left_child_idx += 2

        root_idx += 1
        root = node_arr[root_idx]
    return node_arr[0]
