from TreeNode import *


class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowest_common_ancestor(self, root, p, q):
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)
            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


def main():
    root = convert_list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    solution = Solution()
    print(solution.lowest_common_ancestor(root, root.left.right, root.left))


main()
