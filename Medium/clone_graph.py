"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# BFS
def cloneGraph1(node):
    if not node:
        return 
    nodeCopy = Node(node.label, [])
    dic = {node: nodeCopy}
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic: # neighbor is not visited
                neighborCopy = Node(neighbor.label, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                queue.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy
    
# DFS iteratively
def cloneGraph2(node):
    if not node:
        return 
    nodeCopy = Node(node.label, [])
    dic = {node: nodeCopy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.label, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                stack.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy

def cloneGraph(node):
if not node:
    return 
nodeCopy = Node(node.label, [])
dic = {node: nodeCopy}
dfs(node, dic)
return nodeCopy

def dfs(node, dic):
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighborCopy = Node(neighbor.label, [])
            dic[neighbor] = neighborCopy
            dic[node].neighbors.append(neighborCopy)
            dfs(neighbor, dic)
        else:
            dic[node].neighbors.append(dic[neighbor])