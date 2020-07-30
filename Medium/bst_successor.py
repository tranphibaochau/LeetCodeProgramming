"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val

"""

#recurisvely:
def inorderSuccessor(self, root, p):
	if not root: 
		return None
    if root.val>p.val: 
    	return self.inorderSuccessor(root.left,p) or root 
    return self.inorderSuccessor(root.right,p)
#iteratively
def inorderSuccessor(self, root, p):
	#if p has a right child, the successor is the leftmost child of its right child
	if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
    #if p doesn't have a right child, the idea is to keep just one previous node during the inorder traversal. 
    #If that previous node is equal to p, then the current node is a successor of p
    stack, inorder = [], float('inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        for i in stack:
            print(i.val)
        root = stack.pop()
        if inorder == p.val:
            return root
        inorder = root.val
        root = root.right
    return None