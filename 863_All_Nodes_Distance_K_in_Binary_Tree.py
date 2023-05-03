from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    

        q = deque()
        q.append(root)
        hash_map = defaultdict(list)

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    hash_map[node].append(node.left)
                    hash_map[node.left].append(node)
                if node.right:
                    q.append(node.right)
                    hash_map[node].append(node.right)
                    hash_map[node.right].append(node)

        que = deque()
        que.append((0, target))

        visited = set()
        visited.add(target)
        ans = []
        while que:
            dis, val = que.popleft()
            if dis == k:
                ans.append(val.val)
                continue

            for v in hash_map[val]:
                if v not in visited:
                    visited.add(v)
                    que.append((dis+1, v))

        return ans
