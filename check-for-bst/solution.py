import sys
from tabnanny import check


class Node:
    # constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def check_bst(root, min_value, max_value):
    if root == None:
        return True

    if root.data < min_value or root.data > max_value:
        return False

    return check_bst(root.left, min_value, root.data) and check_bst(root.right, root.data, max_value)


def is_bst(root):
    return check_bst(root, -sys.maxsize - 1, sys.maxsize)


root = Node(4, Node(2, Node(1), Node(6)), Node(5, Node(3), Node(9)))

print(is_bst(root))
