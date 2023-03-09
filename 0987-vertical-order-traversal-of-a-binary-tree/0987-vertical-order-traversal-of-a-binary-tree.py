# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res =sorted(self.preOrder(root, 0, 0 , []))
        print(res)
        
        ans = []
        
        l=r=0
        
        
        while  l < len(res):
            col = res[l][0]
            temp = []
            
            while r < len(res) and col == res[r][0]:
                temp.append(res[r][2])
                r += 1
            ans.append(temp)
            l=r
        return ans     

    def preOrder(self, root,c , r, arr):
        
        if not root:
            return 
        
        arr.append([c,r,root.val])
        left = self.preOrder(root.left, c-1, r+1, arr)
        right = self.preOrder(root.right, c + 1 , r +1, arr)
        
        return arr
 
            
        


         





