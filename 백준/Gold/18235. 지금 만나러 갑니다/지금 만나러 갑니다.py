from collections import deque

N, A, B = map(int, input().split())
MAX_DAY = 20

visited_A = [set() for _ in range(MAX_DAY + 1)]
visited_B = [set() for _ in range(MAX_DAY + 1)]


def bfs(start, visited):
    q = deque()
    q.append((start, 0))
    visited[0].add(start)

    while q:
        now, day = q.popleft()
        if day == MAX_DAY:
            continue
        jump = 2 ** day
        for nxt in [now + jump, now - jump]:
            if 1 <= nxt <= N and nxt not in visited[day + 1]:
                visited[day + 1].add(nxt)
                q.append((nxt, day + 1))

bfs(A, visited_A)
bfs(B, visited_B)

# 두 사람이 같은 날에 같은 위치에 있는지 확인
answer = -1
for day in range(MAX_DAY + 1):
    if visited_A[day] & visited_B[day]:  # 교집합 존재
        answer = day
        break

print(answer)
