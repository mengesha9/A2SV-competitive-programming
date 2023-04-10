"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0
        total = 0
        for n in node.children:
            total = max(total, self.dfs(n))

        return total + 1   
        



       