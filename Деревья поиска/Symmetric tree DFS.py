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

def check_symmetry(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.value != right.value:
            return False
        return (is_mirror(left.left, right.right) and is_mirror(left.right, right.left))

    if root is None:
        return True
    return is_mirror(root.left, root.right)

sym_arr = [1, 2, 2, 3, 4, 4, 3]
sym_root = build_tree(sym_arr)
print(check_symmetry(sym_root))

non_sym_arr = [1, 2, 2, 3, None, 3, None]
non_sym_root = build_tree(non_sym_arr)
print(check_symmetry(non_sym_root))