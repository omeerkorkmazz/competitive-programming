def levelOrder(root):
    nums = []
    visited_nodes = []
    visited_nodes.append(root)

    while visited_nodes:
        node = visited_nodes.pop(0)

        if node is not None:
            nums.append(node.data)
            visited_nodes.append(node.left)
            visited_nodes.append(node.right)

    return nums
