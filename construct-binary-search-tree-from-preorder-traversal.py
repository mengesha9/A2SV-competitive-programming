# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(node,value):

            if value > node.val:
                if node.right :
                    dfs(node.right,value)
                else:
                    node.right = TreeNode(value)    
            else:
                if node.left:
                    dfs(node.left,value)
                else:
                    node.left = TreeNode(value)    

        root =TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            dfs(root,preorder[i])

        return root