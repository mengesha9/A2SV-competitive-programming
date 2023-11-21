# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root 

        q = deque()
        q.append(root)

        while q:
            leng = len(q)
            for i in range(leng):
                node = q.popleft()
                tmp = node.left
                node.left = node.right
                node.right = tmp
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root                 
        