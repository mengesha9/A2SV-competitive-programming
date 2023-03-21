# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.dfs(root1, root2)

    def dfs(self, node1, node2):

        if not node1 and not node2:
            return 

        if node1 and node2:
            tree = TreeNode(node1.val + node2.val) 
            tree.left =  self.dfs(node1.left, node2.left) 
            tree.right = self.dfs(node1.right, node2.right) 
        elif node1:
            tree = TreeNode(node1.val)
            tree.left =  self.dfs(node1.left, node2) 
            tree.right = self.dfs(node1.right, node2) 
        elif node2:
            tree = TreeNode(node2.val)
            tree.left =  self.dfs(node1, node2.left) 
            tree.right = self.dfs(node1, node2.right)     

        
 

        return tree




        