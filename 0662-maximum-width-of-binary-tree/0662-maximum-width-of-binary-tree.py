# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, r, index, arr):
        if not root:
            return 
        arr.append([r, index, root.val])   

        left = self.inorder(root.left, r+1 , 2*index +1, arr) 
        right = self.inorder(root.right, r+1, 2*index + 2 ,arr)

        return arr

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = sorted(self.inorder( root, 0, 0, []))
        
        print(res)

        i , j , n = 0, 0, len(res)
        width = 0
        while i < n:
            row = res[i][0]
            idx = res[i][1]

            while j < n and row == res [j][0]  :
                curr = res[j][1]
                width = max(width, curr - idx + 1)

                j += 1
            i = j
        return width         



   



        

    








        