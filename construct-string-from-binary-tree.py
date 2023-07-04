# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:

        def change(node):
            if not node:
                return ""

            result = str(node.val)
            left = change(node.left)
            right = change(node.right)

            if not left and not right:
                return result 

            if not right:
                return result + "(" + left + ")"

            return result + "(" + left + ")(" + right + ")"

        return change(root)