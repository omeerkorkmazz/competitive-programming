'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def reverseLevelOrder(root):
    nums = []
    visited_nodes = []
    visited_nodes.append(root)

    while visited_nodes:
        node = visited_nodes.pop(0)

        if node is not None:
            nums.append(node.data)
            visited_nodes.append(node.right)
            visited_nodes.append(node.left)

    nums.reverse()
    return nums
