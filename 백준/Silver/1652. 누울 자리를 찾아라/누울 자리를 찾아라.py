N = int(input())
arr = [list(input()) for _ in range(N)]
i = 0
j = 0
cnt = 0
cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '.':
            cnt += 1
            if j == N-1:
                if cnt >= 2:
                    cnt1 += 1
                cnt = 0
        elif arr[i][j] != '.':
            if cnt >= 2:
                cnt1 += 1
            cnt = 0
print(cnt1, end=' ')
cnt = 0
cnt1 = 0

for i in range(N):
    for j in range(N):
        if arr[j][i] == '.':
            cnt += 1
            if j == N-1:
                if cnt >= 2:
                    cnt1 += 1
                cnt = 0
        elif arr[j][i] != '.':
            if cnt >= 2:
                cnt1 += 1
            cnt = 0
print(cnt1)