"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <--- 1
 /   \
2     3         <--- 3
 \     \
  5     4       <--- 4

"""

#the idea is to do a simple level traversal using breadth-first search, then only keep the right-most element for each level
def rightSideView(self, root):
    result = []
    if not root:
        return None
    queue = [root, None]
    level_queue = []
    while len(queue)>0:
        node = queue.pop(0)
        if not node:
            result.append(level_queue[-1].val)
            if len(queue) > 0:
                queue.append(None)
                level_queue = []
        else:
            level_queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result