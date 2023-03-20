# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0,0]

            left_value = dfs(node.left)
            right_value = dfs(node.right)
            arr = [0,0]
            total_tilt = abs(left_value[0]-right_value[0]) + left_value[1] + right_value[1]

            total_sum = left_value[0] + right_value[0] + node.val

            arr[0] = total_sum
            arr[1] = total_tilt

            return arr
        res = dfs(root)    
        return res[1]    




