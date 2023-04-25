# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
       
        def dfs(node,arr):
            if not node:
                return 
            if node and len(arr) >= 2 and arr[-2]%2==0:
                self.total += node.val

           
            arr.append(node.val)
           
            dfs(node.left,arr)
           
            dfs(node.right,arr) 
            arr.pop()
            

        print(dfs(root,[]))
     
        return self.total