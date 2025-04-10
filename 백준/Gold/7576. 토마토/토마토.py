M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = [[0, 0]]*(N*M)
rear = -1
front = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            rear += 1
            q[rear] = [i, j]
            visited[i][j] = 1
x = 1
while True:
    if rear == front:
        break
    front += 1
    i, j = q[front]
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            visited[ni][nj] = visited[i][j] + 1
            x = visited[ni][nj]
            arr[ni][nj] = 1
            rear += 1
            q[rear] = [ni, nj]

if 0 in sum(arr, []):
    print(-1)
else:
    print(x-1)