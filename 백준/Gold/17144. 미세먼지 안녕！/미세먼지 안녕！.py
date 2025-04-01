from collections import deque

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dir1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir2 = [[1, 0], [0, 1], [-1, 0], [0, -1]]


q = deque()
air = deque()
for _ in range(T):
    for x in range(R):
        for y in range(C):
            if arr[x][y] > 0:
                q.append((x, y, arr[x][y] // 5))
            elif arr[x][y] == -1:
                air.append((x, y))
    while q:
        i, j, dif = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                arr[ni][nj] += dif
                arr[i][j] -= dif

    i, j = air.popleft()
    k = i
    for di, dj in dir1:
        ni, nj = i + di, j + dj
        if 0 <= ni <= k and 0 <= nj < C and arr[ni][nj] != -1:
            while 0 <= ni <= k and 0 <= nj < C and arr[ni][nj] != -1:
                if arr[i][j] == -1:
                    arr[ni][nj] = 0
                else:
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                i, j = ni, nj
                ni, nj = i + di, j + dj
    i, j = air.popleft()

    k = i
    for di, dj in dir2:
        ni, nj = i + di, j + dj
        if k <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
            while k <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                if arr[i][j] == -1:
                    arr[ni][nj] = 0
                else:
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                i, j = ni, nj
                ni, nj = i + di, j + dj

cnt = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            cnt += arr[i][j]
print(cnt)
