class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indegree = [0] * len(quiet)
        graph = defaultdict(list)
        index = defaultdict(int)
        for i, v in enumerate(quiet):
            index[v] = i

        for u, v in richer:
            graph[v].append(u)
            indegree[v] += 1

        answer = [-1] * len(quiet)

        def dfs(k):
            if answer[k] != -1:
                return answer[k]

            ans = quiet[k]
            for m in graph[k]:
                tmp = dfs(m)
                if quiet[tmp] < ans:
                    ans = quiet[tmp]
                    answer[k] = tmp

            if answer[k] == -1:
                answer[k] = k

            return answer[k]

        for i in range(len(quiet)):
            dfs(i)

        return answer