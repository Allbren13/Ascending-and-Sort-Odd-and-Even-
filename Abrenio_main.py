import os
import tkinter as tk
from tkinter import Canvas, messagebox


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)

    def _insert_recursively(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
                new_node.parent = current
            else:
                self._insert_recursively(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                new_node.parent = current
            else:
                self._insert_recursively(current.right, new_node)

    def in_order(self):
        result = []
        self._in_order_recursively(self.root, result)
        return result

    def _in_order_recursively(self, current, result):
        if current:
            self._in_order_recursively(current.left, result)
            result.append(current)
            self._in_order_recursively(current.right, result)

    def find_sibling(self, current):
        if not current.parent:
            return None
        if current.parent.left == current:
            return current.parent.right
        else:
            return current.parent.left

    def calculate_properties(self):
        nodes_in_order = self.in_order()
        results = []
        for node in nodes_in_order:
            parent_value = node.parent.value if node.parent else 'NULL'
            sibling = self.find_sibling(node)
            sibling_value = sibling.value if sibling else 'NULL'
            left_value = node.left.value if node.left else 'NULL'
            right_value = node.right.value if node.right else 'NULL'
            degree = sum(child is not None for child in [node.left, node.right])
            depth = self._calculate_depth(node)
            results.append((node.value, parent_value, sibling_value, left_value, right_value, degree, depth))
        return results

    def _calculate_depth(self, node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth


def read_file_data(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        values = []
        for line in lines:
            line = line.strip()
            if line:
                try:
                    value = int(line)
                    values.append(value)
                except ValueError:
                    messagebox.showerror("Data Error", f"The line '{line}' contains a non-integer value.")
                    return []
        return values
    except FileNotFoundError:
        messagebox.showerror("File Error", f"The file '{file_name}' was not found.")
        return []


def draw_tree(canvas, node, x, y, dx):
    if node:
        if node.parent is None:
            node_color = "cyan"  # Root node
        elif node.left is None and node.right is None:
            node_color = "green"  # Leaf node
        else:
            node_color = "yellow"  # Internal node

        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=node_color, outline="black", width=2, tags="node")
        canvas.create_text(x, y, text=str(node.value), tags="node")

        if node.left:
            canvas.create_line(x, y, x - dx, y + 60, tags="line")
            draw_tree(canvas, node.left, x - dx, y + 60, dx // 2)
        if node.right:
            canvas.create_line(x, y, x + dx, y + 60, tags="line")
            draw_tree(canvas, node.right, x + dx, y + 60, dx // 2)


def display_tree(bst):
    root = tk.Tk()
    root.title("Binary Search Tree Visualization")

    canvas = Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    if bst.root:
        draw_tree(canvas, bst.root, 400, 50, 200)

    def refresh_tree():
        canvas.delete("node")
        canvas.delete("line")
        draw_tree(canvas, bst.root, 400, 50, 200)



    root.mainloop()


def main():
    while True:
        file_name = input("Enter the name of the file (including its extension): ").strip()
        if os.path.exists(file_name):
            break
        else:
            print(f"Error: The file '{file_name}' does not exist. Please try again.")

    values = read_file_data(file_name)

    if values:
        bst = BST()
        for value in values:
            bst.insert(value)

        properties = bst.calculate_properties()

        header = ["Node", "Parent", "Sibling", "Left Child", "Right Child", "Degree", "Depth"]
        print("{:<6} {:<6} {:<7} {:<10} {:<11} {:<6} {:<5}".format(*header))

        for prop in properties:
            print("{:<6} {:<6} {:<7} {:<10} {:<11} {:<6} {:<5}".format(*prop))

        display_tree(bst)


if __name__ == "__main__":
    main()