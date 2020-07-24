"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example call:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.heap = []
        self.index = -1
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.heap.append(root.val)
            inorder(root.right)
        inorder(root)
                
        
            
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index+=1
        return self.heap[self.index]
        
    
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index +1 < len(self.heap)