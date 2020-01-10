####################################################################################################################################
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#Note: A leaf is a node with no children.
####################################################################################################################################


class Solution:
	#Recursive solution
    def minDepth (self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = float('inf')
        for c in ([root.left, root.right]):
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth+1

    #Iterative solution
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root),], float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        
        return min_depth 