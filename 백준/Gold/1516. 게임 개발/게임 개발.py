# 게임 개발
# 위상 정렬을 통한 문제 해결이 필요해 보임
# 그러면 우선 처음에 받아올 것을 한 번 정리해서 한 번에 처리가 가능하게 바꿀 수 있으면 매우 간단할 것 같음

from collections import deque
import sys
input = sys.stdin.readline

# 건물 개수 입력
N = int(input())
# 각 건물의 후속 건물들을 저장하는 인접 리스트
graph = [[] for _ in range(N+1)]
# 각 건물의 진입 차수(해당 건물을 짓기 위해 필요한 선행 건물 수)
indegree = [0]*(N+1)
# 각 건물의 건설 시간
cost = [0]*(N+1)
# 각 건물을 완성하는데 필요한 최소 시간
dp = [0]*(N+1)

# 각 건물의 정보 입력
for i in range(1, N+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]  # 건물 i의 건설 시간
    # 선행 건물들 처리 (마지막 -1 제외)
    for pre in data[1:-1]: # # 마지막 -1은 종료 신호
        graph[pre].append(i)  # 선행 건물 pre 완성 후 건물 i 건설 가능
        indegree[i] += 1      # 건물 i의 진입 차수 증가

# 위상 정렬을 위한 큐 초기화
q = deque()
# 선행 건물이 없는 건물들을 큐에 추가
for i in range(1, N+1):
    if indegree[i] == 0:
        dp[i] = cost[i]  # 선행 건물이 없으면 자체 건설 시간이 완성 시간
        q.append(i)

# 위상 정렬 수행
while q:
    u = q.popleft()
    # 현재 건물 u 완성 후 건설 가능한 모든 건물들 처리
    for v in graph[u]:
        # 건물 v 완성 시간 = max(기존 완성 시간, 건물 u 완성 시간 + 건물 v 건설 시간)
        # 건물 v를 짓기 위해 필요한 최소 시간은,
        # 그 전의 선행 건물들 중 가장 오래 걸리는 선행 건물이 다 지어진 후
        # cost[v]만큼 더해진 값이어야 한다.
        dp[v] = max(dp[v], dp[u] + cost[v])
        indegree[v] -= 1  # 건물 v의 진입 차수 감소
        if indegree[v] == 0:  # 모든 선행 건물이 완성된 경우
            q.append(v)

# 각 건물의 완성 시간 출력
print(*dp[1:], sep='\n')

