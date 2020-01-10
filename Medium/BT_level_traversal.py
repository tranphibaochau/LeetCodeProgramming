#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels =[]
        if not root:
            return levels
        def helper (root, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            if root.left !=None:
                helper(root.left, level+1)
            if root.right != None:
                helper(root.right, level+1)
        
        helper(root, 0)
        return levels