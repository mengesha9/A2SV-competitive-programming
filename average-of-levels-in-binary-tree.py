# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        qu = deque()
        qu.append(root)
        arr = []
        while qu:
            leng = len(qu)
            sum_= 0
            count = 0
            for i in range(leng):
                node = qu.popleft()
                sum_ += node.val
                count += 1
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            if count != 0:

               arr.append(sum_/count)


        return arr