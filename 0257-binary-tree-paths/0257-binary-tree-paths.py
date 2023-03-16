# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def paths(node, arr ):
            if not node:
                return 
            if  not node.left and not node.right:
                arr.append(str(node.val))
                
                res .append('->'.join(arr))
                arr.pop()

                return 

            arr .append(str(node.val))
            
            paths(node.left, arr) 

            paths(node.right, arr)
            arr.pop()

        paths(root,[]) 

        return res   

 

        