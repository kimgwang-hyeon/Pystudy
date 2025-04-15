from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

players = [i for i in range(N)]  # 축구를 하는 사람들의 인덱스를 만들어주자
min_diff = float('inf')  # 최소 값을 무한대로 설정

for team_start in combinations(players, N // 2):  # 스타트 팀은 반
    team_link = [p for p in players if p not in team_start]  # 나머지 반은 링크 팀

    start_score = 0
    link_score = 0

    for i in range(N // 2):  # 팀원 모두의 2명을 뽑는 조합을 보면서
        for j in range(i + 1, N // 2):
            a, b = team_start[i], team_start[j]
            start_score += S[a][b] + S[b][a]  # 스타트 팀 능력치에 추가

            a, b = team_link[i], team_link[j]
            link_score += S[a][b] + S[b][a]  # 링크 팀 능력치에 추가

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

    if min_diff == 0:
        break

print(min_diff)
