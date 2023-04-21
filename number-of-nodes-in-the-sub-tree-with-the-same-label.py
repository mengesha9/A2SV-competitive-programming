class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        ans = [0] * n

        def dfs(node, parent):
            count = defaultdict(int)
            for child in adj[node]:
                if child == parent:
                    continue
                for label, cnt in dfs(child, node).items():
                    count[label] += cnt
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            return count

        dfs(0, -1)
        return ans