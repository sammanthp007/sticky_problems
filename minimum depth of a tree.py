# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A.left == None and A.right == None:
            return 1
        elif A.left == None:
            return 1 + self.minDepth(A.right)
        elif A.right == None:
            return 1 + self.minDepth(A.left)
        else:
            return min(1 + self.minDepth(A.left), 1 + self.minDepth(A.right))