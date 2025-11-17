from collections import deque
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
    if root is None:
        return True
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        left, right = 0, level_size - 1
        while left < right:
            left_node = level_nodes[left]
            right_node = level_nodes[right]
            if left_node is None and right_node is None:
                left += 1
                right -= 1
                continue
            if left_node is None or right_node is None:
                return False
            if left_node.value != right_node.value:
                return False
            left += 1
            right -= 1

    return True

sym_arr = [1, 2, 2, 3, 4, 4, 3]
sym_root = build_tree(sym_arr)
print(check_symmetry(sym_root))

non_sym_arr = [1, 2, 2, 3, None, 3, None]
non_sym_root = build_tree(non_sym_arr)
print(check_symmetry(non_sym_root))