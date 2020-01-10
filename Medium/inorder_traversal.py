# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Solution 1: using recursive function (trivial)
class Solution:
    def helper (self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
#Solution 2: implement iterative function by using stack
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
        	#keep pushing the left tree
            stack.append(root)
            root = root.left
        #return when stack is empty
        if not stack:
            return res
        #pop the node that is the leftest node first
        node = stack.pop()
        #append to the result array
        res.append(node.val)
        #go to the right tree and iteratively add items in again
        root = node.right
        