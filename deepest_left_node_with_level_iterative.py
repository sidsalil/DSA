class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


def deepest_left_node(root):
    if not root:
        return None, 0

    max_level = 0
    deepest_node = None

    stack = [(root, 1)]
    while stack:
        node, level = stack.pop()

        if node.left:
            stack.append((node.left, level + 1))
            if level > max_level:
                max_level = level
                deepest_node = node.left

        if node.right:
            stack.append((node.right, level + 1))

    return deepest_node, max_level

# Example usage:
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.left.left = Node('I')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
root.right.right.right = Node('J')
root.right.left.left = Node('H')

node, level = deepest_left_node(root)
print("Deepest left node:", node.value)
print("Level:", level)
