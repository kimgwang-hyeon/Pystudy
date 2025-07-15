from collections import deque

N, K = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
dq = deque()
dq.append(N)
visited[N] = 0

while dq:
    now = dq.popleft()
    if now == K:
        break

    for next in [now * 2, now - 1, now + 1]:
        if 0 <= next < MAX and visited[next] == -1:
            if next == now * 2:
                visited[next] = visited[now]
                dq.appendleft(next)
            else:
                visited[next] = visited[now] + 1
                dq.append(next)

print(visited[K])
