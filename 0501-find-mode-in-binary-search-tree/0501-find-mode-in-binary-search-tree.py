# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:


        arr=[]

        def help(node):
            if not node:
                return 
            help(node.left)
            arr.append(node.val)
            help(node.right)
        help(root)
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        y=set(arr)  
        res=[]
        print(arr)
        print(d)
        print(y)
        
        for  i in y:
            if res and d[i] >d[res[-1]]:
                while res:
                    res.pop()      
                res.append(i)
            elif res and  d[i] < d[res[-1]] :
                continue
            elif res and d[i]==d[res[-1]]:
                res.append(i)
            else:
                res.append(i)  
        return res          
       