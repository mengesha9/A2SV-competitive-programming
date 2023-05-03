# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0,float("-inf")]

            left = dfs(node.left)
            right = dfs(node.right)
    
            total = node.val + max(left[0],0) + max(0,right[0])
            path_sum = node.val + max(left[0], right[0], 0)

            curr = max(left[1],right[1],total)
        

            return [path_sum,curr]

        ans = dfs(root)

        return ans[1]