import os


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.right, new_node)

    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node)
            self._in_order_recursive(node.right, result)

    def find_sibling(self, node):
        if not node.parent:
            return None
        if node.parent.left == node:
            return node.parent.right
        else:
            return node.parent.left

    def compute_properties(self):
        in_order_nodes = self.in_order_traversal()
        output = []
        for node in in_order_nodes:
            parent = node.parent.key if node.parent else 'NULL'
            sibling_node = self.find_sibling(node)
            sibling = sibling_node.key if sibling_node else 'NULL'
            left_child = node.left.key if node.left else 'NULL'
            right_child = node.right.key if node.right else 'NULL'
            degree = sum(child is not None for child in [node.left, node.right])
            depth = self._compute_depth(node)
            output.append((node.key, parent, sibling, left_child, right_child, degree, depth))
        return output

    def _compute_depth(self, node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [int(line.strip()) for line in data]


def main():
    filename = "DATA.txt"
    # Check if the file exists in the current directory or provide a full path
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found in the current directory.")
        return

    data = read_data_from_file(filename)

    bst = BinarySearchTree()
    for value in data:
        bst.insert(value)

    properties = bst.compute_properties()

    # Print table header with alignment
    header = ["Node", "Parent", "Sibling", "Left Child", "Right Child", "Degree", "Depth"]
    print("{:<6} {:<6} {:<7} {:<10} {:<11} {:<6} {:<5}".format(*header))

    # Print each row with alignment
    for prop in properties:
        print("{:<6} {:<6} {:<7} {:<10} {:<11} {:<6} {:<5}".format(*prop))


if __name__ == "__main__":
    main()
