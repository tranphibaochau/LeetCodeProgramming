class TreeNode:
	def __init__(self, val):
		self.val = val
		self.children = []

class Solution:
	def maxTenureTeam(self, root):
		if not root:
			return 0
		dict = {}
		def DFS(root, dict):
			if not root:
				return
			elif len(root.children) == 0:
				return
			elif root.val not in dict:
				dict[root.val] = [root.val]
			for c in root.children:
				dict[root.val].append(c.val)
				DFS(c, dict)
		DFS(root, dict)
		print(dict)

sol = Solution()
t = TreeNode(5)
t.children = [TreeNode(19), TreeNode(7), TreeNode(8)]
t1 = t.children[0]
t1.children = [TreeNode(4), TreeNode(10), TreeNode(16)]
t2 = t.children[1]
t2.children = [TreeNode(11), TreeNode(30), TreeNode(8)]
t3 = t1.children[0]
t3.children = [TreeNode(1), TreeNode(8), TreeNode(12)]
sol.maxTenureTeam(t)





