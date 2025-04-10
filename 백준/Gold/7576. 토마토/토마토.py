from collections import deque

def tomato():
    # 토마토 익은 날 수를 넣어줄 리스트
    ripe = [[0] * M for _ in range(N)]
    q = deque()  # 큐 선언
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:  # 익은 토마토라면
                q.append((i, j))    # 큐에 모두 넣어주기
                ripe[i][j] = 1      # 해당 값은 모두 1일차에 익은 토마토
            elif box[i][j] == -1:   # -1이라면
                ripe[i][j] = -1     # 애초에 익을 수 없음
    # bfs 돌아주기
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = ti+di, tj+dj
            # 범위 내에서, 토마토가 익지 않았고, 일수 추가도 안되었다면
            if 0<=ni<N and 0<=nj<M and box[ni][nj] == 0 and ripe[ni][nj] == 0:
                q.append([ni, nj])  # 새로 넣어주고
                ripe[ni][nj] = ripe[ti][tj] + 1 # 일수 추가
    return ripe


# 입력 받기
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
t = True        # 토마토가 다 익었는지 확인할 변수
max_val = 0     # 최댓값 초기화
ripe = tomato()
# 방문표시 중, 최댓값 찾기
for i in range(N):
    for j in range(M):
        max_val = max(max_val, ripe[i][j])  # 최댓값 할당
        if ripe[i][j] == 0:     # 안익은게 하나라도 있으면
            t = False           # t는 False

if t:
    print(max_val-1)
else:
    print(-1)