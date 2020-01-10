#########################################################################################################
#Given a binary tree, determine if it is a valid binary search tree (BST).
#
#Assume a BST is defined as follows:
#.   The left subtree of a node contains only nodes with keys less than the node's key.
#.   The right subtree of a node contains only nodes with keys greater than the node's key.
#.   Both the left and right subtrees must also be binary search trees.
#########################################################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#the idea is going recursively, check the value of the left child to be smaller than the lower bound (the smallest value of all its predecessors), 
#and the right child to be bigger than the upper bound
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)