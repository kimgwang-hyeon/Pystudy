import heapq


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))
visited = [False] * (N + 1)
pq = [(0, 1)]
total_cost = 0
while pq:
    cost, node = heapq.heappop(pq)
    if visited[node]:
        continue
    visited[node] = True
    total_cost += cost
    for next_cost, neighbor in graph[node]:
        if not visited[neighbor]:
            heapq.heappush(pq, (next_cost, neighbor))
print(total_cost)
