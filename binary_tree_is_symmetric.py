# is a tree symmetric?

def is_symmetric(root):
    if root == None:
        return True
    else:
        return are_images(root.left, root.right)

def are_images(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif node1 == None or node2 == None:
        return False
    if (node1.val == node2.val) and are_images(node1.left, node2.right) and are_images(node1.right, node2.left):
        return True
    else:
        return False
