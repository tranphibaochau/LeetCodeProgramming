# Definition for a binary tree node.
from collections import deque
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def add_left_child(self, value):
		self.left = TreeNode(value)
	def add_right_child(self, value):
		self.right = TreeNode(value)

class Solution:
	def list_to_tree(self, tree_list):
		if len(tree_list) == 0:
			raise Exception('Cannot build an empty tree')
		elif tree_list[0] is None:
			raise Exception('Root cannot be null')
		while tree_list:
			root = TreeNode(tree_list.pop(0))
			curr = root
			curr.add_left_child(tree_list.pop[0])
			curr.add_right_child(tree_list.pop[0])
			if curr.left is not None:
				curr = curr.left
			elif curr.right is not None:
				curr = curr.right

		return root




	def verticalOrder(self, root):
		nodes = {}
        #while root not None:

l = [9, 8]
solution = Solution()
a = solution.list_to_tree(l)
print(a.val)
