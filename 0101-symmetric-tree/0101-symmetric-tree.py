# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        depth_right = 0
        depth_left = 0
        
        left = root
        right = root

        while left and left.left:
            left =left.left
            depth_left += 1
        while right and right.right:
            right = right.right
            depth_right += 1  

        if depth_right != depth_left:
            return False      

        arr1 = self.right(root, [])
        arr2 = self.left(root, [])
        
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True        

    def right(self, root, arr):
        if root == None:
            return 
        right = self.right(root.right, arr) 
        arr.append(root.val)   
        left = self.right(root.left, arr)

        return arr

    def left(self, root, arr):
        if root == None:
            return 
        left = self.left(root.left, arr) 
        arr.append(root.val)   
        right = self.left(root.right, arr)

        return arr





        