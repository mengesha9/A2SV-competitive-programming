# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        ref = [p.val,q.val]

        def dfs(node):
            if not node:
                return 0,TreeNode()
            count = 0

            right, right_node= dfs(node.right)
            left,left_node  = dfs(node.left)
            if right == 2:
                return right , right_node
            if left == 2:
                return left,left_node

            count = left+right    
            count += 1 if node.val in ref else 0

        
            return count,node
        count , node = dfs(root)
        
        return node      
            
               
             




        
        
