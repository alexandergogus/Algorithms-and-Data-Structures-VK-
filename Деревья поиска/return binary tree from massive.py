class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(array, i=0):
    if i >= len(array):
        return None
    root = TreeNode(array[i])
    root.left = build_tree(array, 2*i+1)
    root.right = build_tree(array, 2*i+2)
    return root

def print_result(root):
    if root:
        print_result(root.left)
        print(root.value, end=' ')
        print_result(root.right)

arr = [8, 9, 11, 7, 16, 3, 1]
root = build_tree(arr)
print_result(root)