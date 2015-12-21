# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# see if the value == sum1, if it is then append it to the result_lis, elif sum(
class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        self.result_lis = []
        temp_lis = []
        self.pathSumFrom(root, sum1, temp_lis)
        return self.result_lis
    
    def pathSumFrom(self, node, sum1, temp_lis):
        if node == None:
            return
        if node.left == None and node.right == None:
            temp_lis.append(node.val)
            temp_sum = sum(temp_lis)
            if temp_sum == sum1:
                self.result_lis.append(temp_lis)
            return
        temp_lis.append(node.val)
        self.pathSumFrom(node.left, sum1, temp_lis[:])
        self.pathSumFrom(node.right, sum1, temp_lis[:])