class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(array, i=0):
    if i >= len(array) or array[i] is None:
        return None
    root = TreeNode(array[i])
    root.left = build_tree(array, 2 * i + 1)
    root.right = build_tree(array, 2 * i + 2)
    return root


def max_min_multiplication(root):
    if root is None:
        return 0

    def find_min(node):
        if node is None:
            return float('inf')
        return min(node.value, find_min(node.left), find_min(node.right))

    def find_max(node):
        if node is None:
            return float('-inf')
        return max(node.value, find_max(node.left), find_max(node.right))

    min_val = find_min(root)
    max_val = find_max(root)
    if min_val == float('inf') or max_val == float('-inf'):
        return 0

    return min_val * max_val

arr1 = [8, 9, 11, 7, 16, 3, 1]
root1 = build_tree(arr1)
print(max_min_multiplication(root1))

arr2 = [10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]
root2 = build_tree(arr2)
print(max_min_multiplication(root2))

arr3 = [1, 2, 3]
root3 = build_tree(arr3)
print(max_min_multiplication(root3))

arr4 = [1]
root4 = build_tree(arr4)
print(max_min_multiplication(root4))

arr5 = [1, 2]
root5 = build_tree(arr5)
print(max_min_multiplication(root5))