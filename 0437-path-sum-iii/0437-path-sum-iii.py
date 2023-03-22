# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        hash_map = defaultdict(int)
        hash_map[0] = 1
        self.count = 0
        def path_III(node, total):
            if not node:
                return 
            total += node.val    
            if total - targetSum in hash_map:
                self.count += hash_map[total-targetSum]
                 

            hash_map[total] += 1
            path_III(node.left, total) 
         
            path_III(node.right, total) 

            hash_map[total] -= 1

            if hash_map[total] == 0:
                del hash_map[total]

        path_III(root, 0) 

        return self.count   


