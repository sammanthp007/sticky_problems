# check if a binary tree is BST or not

# input: root of a binary tree
# each nodes are implemented as
class NodeType(object):
    def __init__(self, d=None):
        self.data = d
        self.left_child = None
        self.right_child = None

# output: Boolean indicating if the tree is BST or not
# working: concept -> a binary tree is BST if for each node 
# 1) its left child has data that is smaller than its;
# 2) if there is a right child, then right child is 
# 3) each of its child are also BST
high = float('inf')
low = float('-inf')

def is_BST(root_node, high, low):
    if root_node == None:
        return True
    if root.data < high and root.data > low and is_BST(root_node.left_child, root_node.data, low) and is_BST(root_node.right_child, high, root_node.data):
        return True
    return False