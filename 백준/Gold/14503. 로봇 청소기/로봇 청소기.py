from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque([(r, c, d)])
turn = [[3, 2, 1, 0],
        [0, 3, 2, 1],
        [1, 0, 3, 2],
        [2, 1, 0, 3]]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
while q:
    i, j, d = q.popleft()
    if arr[i][j] == 0:
        arr[i][j] = 2
        ans += 1
    for x in turn[d]:
        di, dj = dirs[x]
        ni, nj = i + di, j + dj
        if arr[ni][nj] == 0:
            q.append((ni, nj, x))
            break
    else:
        if d == 0:
            if arr[i+1][j] == 1:
                break
            else:
                q.append((i+1, j, d))
        elif d == 1:
            if arr[i][j-1] == 1:
                break
            else:
                q.append((i, j-1, d))
        elif d == 2:
            if arr[i-1][j] == 1:
                break
            else:
                q.append((i-1, j, d))
        elif d == 3:
            if arr[i][j + 1] == 1:
                break
            else:
                q.append((i, j + 1, d))
print(ans)
