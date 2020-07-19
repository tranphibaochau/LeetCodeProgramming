
#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).


from collections import deque

def levelOrderBottom(self, root):
    result = []
    level_queue = deque([root, None])
    level_list = []
    if not root:
        return result
    while len(level_queue) > 0:
        node = level_queue.popleft()
        if node: #if it's not None, meaning the delimeter
            level_list.append(node.val)
            if node.left:
                level_queue.append(node.left)
            if node.right:
                level_queue.append(node.right)
        else:
            result.append(level_list)
            if len(level_queue) > 0:
                level_queue.append(None)
            level_list = []
    return result[::-1]