# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append((0,root))
        total = 0
        while q:
            leng = len(q)
            for i in range(leng):
                d,node = q.popleft()
                if d == -1 and not node.left and not node.right:
                    total += node.val

                if node.left:    
                    q.append((-1,node.left))
                if node.right:
                    q.append((1,node.right))
        return total 

                    

        