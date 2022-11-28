class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # recursively print out tree nodes
    def __str__(self):
        if not self:
            return
        s = ("{TreeNode{val: " + str(self.val))
        if self.left:
            s += ", left: " + str(self.left)
        else:
            s += ", left: None"
        if self.right:
            s += ", right: " + str(self.right)
        else:
            s += ", right: None"
        s += "}"
        return s


# convert a list of integers to a binary tree
def convert_list_to_tree(tree_list):
    # convert all integers into TreeNode objects
    for i, n in enumerate(tree_list):
        if n is not None:
            tree_list[i] = TreeNode(n)
    root = tree_list[0]

    # for each TreeNode object in the list, locate its parent and link them together
    for i in range(1, len(tree_list)):
        if tree_list[i] is not None:
            if i % 2 == 0:
                tree_list[(i // 2) - 1].right = tree_list[i]
            else:
                tree_list[(i // 2)].left = tree_list[i]
    return root
