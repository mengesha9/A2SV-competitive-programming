# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        arr = self.average(root)

        return arr[2]

    def average(self, root):

        if not root:
            return [0,0,0]  

        arrleft = self.average(root.left)
        arrright = self.average(root.right)

        total_sum = root.val + arrleft[0] + arrright[0]
        total_nodes = arrleft[1] + arrright[1] + 1
        total_count = arrleft[2] + arrright[2]

        average = total_sum // total_nodes
        arr = [total_sum, total_nodes, total_count]

        if average == root.val:
            arr[-1] += 1

        return arr