class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dic = {
            1: [[0, -1], [0, 1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[0, 1], [-1, 0]]
        }
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r == n - 1 and c == m - 1:
                return True

            visited.add((r, c))

            for node in dic[grid[r][c]]:
                row = r + node[0]
                col = c + node[1]
                if 0 <= row < n and 0 <= col < m and (row, col) not in visited:
                    for back_node in dic[grid[row][col]]:
                        if row + back_node[0] == r and col + back_node[1] == c:
                            if dfs(row, col):
                                return True

            return False

        return dfs(0, 0)