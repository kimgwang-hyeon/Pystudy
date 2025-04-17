def dfs(i, j):
    if j == 0:
        return True

    for dj, di in [(-1, -1), (-1, 0), (-1, 1)]:
        nj, ni = j + dj, i + di
        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == '.':
            grid[ni][nj] = 'x'
            if dfs(ni, nj):
                return True
    return False


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
result = 0
for i in range(R):
    if dfs(i, C - 1):
        result += 1
print(result)
