
#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).



from collections import deque
def zigzagLevelOrder(self, root):
    result = []
    level_queue = deque([root, None]) #overall queue, use None to separate each level (when the queue pops None, it signals that this is the end of a level)
    level_list = deque() #the list of nodes for each level
    left_right = True #boolean value to determine whether or not we're appending from the left or the right of the deque
    if not root:
        return result
    while len(level_queue) > 0:
        node = level_queue.popleft()
        if node: #if it's not None, meaning the delimeter
            if left_right:
                level_list.append(node.val)
            if not left_right:
                level_list.appendleft(node.val)
            if node.left:
                level_queue.append(node.left)
            if node.right:
                level_queue.append(node.right)
        else:
            result.append(level_list)
            if len(level_queue) > 0:
                level_queue.append(None)
            level_list = deque()
            left_right = not left_right
    return result
            
            
                
                