# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
 
        if not root:
            return []
        length=self.depth(root)
        print(length)

        stack=[]
        stack.append([root])  
        res = []
        res.append(root.val)
        while length >= 0 :
            node = stack.pop()
            arr = []
            temp = []
            for n in node:
                if n.left:
                    arr.append(n.left.val)
                    temp.append(n.left)
                if n.right:
                    arr.append(n.right.val)
                    temp.append(n.right)
            if arr:        
                res.append(arr[-1])
                
            stack.append(temp)

            length -= 1
        # print(res)
        return res  
    def depth(self, root):

        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        return max(left, right) + 1    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        