class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(array, i=0):
    if i >= len(array):
        return None
    root = TreeNode(array[i])
    root.left = build_tree(array, 2 * i + 1)
    root.right = build_tree(array, 2 * i + 2)
    return root

def min_depth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(min_depth(root.left),min_depth(root.right))
    if root.left is not None:
        return 1 + min_depth(root.left)
    if root.right is not None:
        return 1 + min_depth(root.right)

arr1 = [1, 2, 3]
root1 = build_tree(arr1)
print(min_depth(root1))

arr2 = [1, 2, None, 3]
root2 = build_tree(arr2)
print(min_depth(root2))

arr3 = [1, 2, 3, 4, 5, 6, 7]
root3 = build_tree(arr3)
print(min_depth(root3))

print(min_depth(None))