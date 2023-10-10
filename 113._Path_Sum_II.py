# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node,arr):

            if not node.left and not node.right :
                arr.append(node.val)
                if sum(arr) == targetSum  :
                    res.append(arr.copy())
    
                arr.pop()    
                return 
           
            arr.append(node.val)
            if node.left:  
                dfs(node.left , arr)
            if node.right:    
                dfs(node.right , arr) 
            arr.pop()

        dfs(root,[])
        return res 


        
