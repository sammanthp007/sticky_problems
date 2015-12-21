# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        res = 0
        temp_lis = []
        return self.hasPathSumFrom(A, B, temp_lis)
    
    def hasPathSumFrom(self, node, sum1, temp_lis):
        # case 1: when node is none
        if node == None:
            return False
        # case 2: when leaf node
        if node.left == None and node.right == None:
            temp_lis.append(node.val)
            temp_sum = sum(temp_lis)
            if sum1 == temp_sum:
                return True
            return False
        # case 3: when not leaf
        temp_lis.append(node.val)
        return self.hasPathSumFrom(node.left, sum1, temp_lis[:]) or self.hasPathSumFrom(node.right, sum1, temp_lis[:])
        
        
        
        
        
        