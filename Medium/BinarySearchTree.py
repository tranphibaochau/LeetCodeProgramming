# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def 


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            if start > end:
                return [None, ]
            results = []
            for i in range(start, end+1):  # pick the root
                left_tree = helper(start, i-1) #recursively create left sub-trees
                right_tree = helper(i+1, end) #recursively create right sub-trees
                
                #merge them in together afterwards
                for l in left_tree:
                    for r in right_tree:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        print(current_tree)
                        results.append(current_tree)
            return results
        return helper(1, n) if n else []
            