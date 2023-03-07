# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = [0]
        res = [-1]
        
        self.helper( root, k, count, res)

        return res[0]

    def helper(self, root, k, count, res):
        if not root:
            return

        left = self.helper(root.left, k, count, res)    
        count[0] += 1

        if count[0] == k:
            res[0] = root.val
            
        right = self.helper(root.right, k, count, res)



        

    

        