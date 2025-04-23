from collections import deque


def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        i, j, rock = q.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj][rock] == 0:
                    visited[ni][nj][rock] = visited[i][j][rock] + 1
                    q.append((ni, nj, rock))

                elif arr[ni][nj] == 1 and rock == 0 and visited[ni][nj][1] == 0:
                    visited[ni][nj][1] = visited[i][j][rock] + 1
                    q.append((ni, nj, 1))

    result0 = visited[N - 1][M - 1][0]
    result1 = visited[N - 1][M - 1][1]

    if result0 == 0 and result1 == 0:
        return -1
    elif result0 == 0:
        return result1
    elif result1 == 0:
        return result0
    else:
        return min(result0, result1)


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

print(bfs())
