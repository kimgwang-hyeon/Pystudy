def dfs(now, path):
    visited[now] = True
    path.append(now)
    next = arr[now]

    if not visited[next]:
        dfs(next, path)
    elif next in path:
        idx = path.index(next)
        result.extend(path[idx:])


N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
visited = [False] * (N + 1)
result = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, [])


print(len(set(result)))
for num in sorted(set(result)):
    print(num)