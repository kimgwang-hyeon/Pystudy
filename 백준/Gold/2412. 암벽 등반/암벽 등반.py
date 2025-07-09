## 백준 2412 암벽 등반
## 그래프 문제인 것 같음
## 인접 그래프를 만들어서 다음에 갈 수 있는 것을 찾다가 실제로 도착하면 끝
## 그렇다면 인접 그래프를 가장 시간 복잡도가 낮게 만들어 보자
## 처음에 그냥 모든 점을 탐색하려고 하니까 시간 초과 나옴
## 이유는? 당연히 O(n^2)의 시간 복잡도를 가지기 때문
## y축 기준으로 정렬한 후 

from collections import defaultdict, deque

n, T = map(int, input().split())
points = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 인접 리스트 생성
adj_list = defaultdict(list)

# y 기준 정렬
points.sort(key=lambda p: p[1])  # (x, y)

# 간선 생성: y 기준 슬라이딩 윈도우
for i in range(n + 1):
    x1, y1 = points[i]

    # 이후 y값이 최대 +2인 애들만 봄
    for j in range(i + 1, n + 1):
        x2, y2 = points[j]
        if y2 - y1 > 2:
            break  # y 차이가 2보다 크면 더 이상 연결 불가

        if abs(x1 - x2) <= 2:
            adj_list[(x1, y1)].append((x2, y2))
            adj_list[(x2, y2)].append((x1, y1))

# BFS
q = deque()
q.append(((0, 0), 0))  # ((x, y), jump_count)
visited = set()
visited.add((0, 0))

found = False

while q:
    (x, y), cnt = q.popleft()

    if y == T:
        print(cnt)
        found = True
        break

    for nx, ny in adj_list[(x, y)]:
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append(((nx, ny), cnt + 1))

if not found:
    print(-1)
