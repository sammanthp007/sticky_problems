# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A == None and B == None:
            return True
        if A == None or B == None:
            return False
        return (A.val == B.val) and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)