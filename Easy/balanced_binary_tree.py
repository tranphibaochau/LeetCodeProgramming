####################################################################################################################################
# Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as:
#    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
####################################################################################################################################

class Solution:
	#Top-down recursive
    def height (self, root):
        if not root:
            return -1
        else:
            return (1 + max(self.height(root.left), self.height(root.right)))
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    #Bottom-up recursive
    def isBalancedHelper(self, root):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self):
        return self.isBalancedHelper(root)[0]

    #Iterative solution
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
