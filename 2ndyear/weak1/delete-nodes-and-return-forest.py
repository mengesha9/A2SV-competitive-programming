# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        arr  = set()
        arr.add(root)
        delete = set(to_delete)
        def preorder(node):
            if node is None:
                return

            if node.val in delete:
                arr.remove(node)

                arr.add(node.left)
                preorder(node.left)

                node.left = None

                arr.add(node.right)
                preorder(node.right)

                node.right = None
            else:

                if node.left :
                    if  node.left.val in delete:
                        arr.add(node.left)

                        preorder(node.left)
                        node.left = None
                    else:
                        preorder(node.left)

                if node.right:
                    if  node.right.val in delete:
                        arr.add(node.right)
                        preorder(node.right)
                        
                        node.right = None
                    else:
                        preorder(node.right)
        preorder(root) 
        res = [] 
        for n in list(arr):
            if n :
                res.append(n)

        return  res  



        





        