from collections import deque


for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    q = deque()
    visited = [[0] * 16 for _ in range(16)]
    q.append((1, 1))
    visited[1][1] = 1
    result = True
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 3:
                    result = False
                    print(f'#{tc} 1')

    if result == True:
        print(f'#{tc} 0')