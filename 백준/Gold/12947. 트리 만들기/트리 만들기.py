# 트리에 관한 문제

N = int(input())
cnt = list(map(int, input().split()))
result = 0

sub = 0


for i in range(N-1, -1, -1):
    if cnt[i] == 1:
        result = max(result, sub + N - i - 1)
        sub = 0
    else:
        sub += 1
result = max(result, sub + N)
print(result)
