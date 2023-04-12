# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        result = []


        def dfs(node,arr):
            arr.append(str(node.val))
            if not node.right and not node.left:

                tmp = ''.join(arr)
                
                result.append(tmp)
            elif node.left and not node.right:
                dfs(node.left,arr)
                
            elif not node.left and node.right:
                dfs(node.right,arr)
               
            else:
                dfs(node.left,arr)
                dfs(node.right,arr)

            arr.pop()       

          

        dfs(root,[])

        print(result)
        total = 0
        for i in range(len(result)):
            total += int(result[i])

        return total   

