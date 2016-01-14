# Write an algorithm to find the ‘next’ node (e.g., in-order successor) of a given node in a binary search tree where each node has a link to its parent.

                 7
             3        9
           1   4    8   10 
         0  2 3  6

# case1: if our current is in the left_ptr of the root node -> the root node is our next element
# case3: if it has a right child then the inorder successor is the left_most of its right child
# case2: if our current is in the right_ptr of the root node -> the first right_parent of parent is the successor

#with link to parent
def inorder_successor(node):
    # case when it has a right parent:
    if node.right_child != None:
        node = node.right_child
        while node.left_child != None:
            node = node.left_child
        return node
    # case when it does not have a right parent
    else:
        while node.parent != None
            parent = node.parent
            # case when it is a left child
            if node == parent.left_child:
                return parent
            node = parent

# with no link to parent
def inorder_successor(root, node):
    if root.data < node.data:
        return inorder_successor(root.right, node)
    else:
        temp = root
        while temp.left != None and node.data < temp.data:
            temp = temp.left
            if temp == node:
                return root
        return inorder_successor(root.left, node)
as