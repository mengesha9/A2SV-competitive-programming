# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            hash_map[total] += 1
            return total
        dfs(root)
        arr = hash_map.keys()
        answer = []
        for key in arr:
            max_fre= hash_map[key]
            if answer and max_fre > hash_map[answer[-1]] :
                while answer :
                    answer.pop()
                answer.append(key)    
            elif (answer and max_fre== hash_map[answer[-1]]) or not answer:
                answer.append(key)
        return answer    


