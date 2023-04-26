n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Create a transposed grid to iterate over columns
transposed_grid = list(zip(*grid))

result = []
for i in range(n):
    for j in range(m):
        # Check if the character is unique in its row
        if grid[ i].count(grid[i][j]) == 1 and grid[i][j] not in grid[i][j+1:]:
            # Check if the character is unique in its column
            if transposed_grid[j].count(grid[i][j]) == 1 and grid[i][j] not in [row[j] for row in grid[i+1:]]:
                result.append(grid[i][j])

print(''.join(result))
