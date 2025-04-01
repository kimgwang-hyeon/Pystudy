N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N-1, 0, -1):
    if arr[i] - K < arr[i-1]:
        cnt += (N-i) * (arr[i-1] - (arr[i] - K))
    elif arr[i] - K > arr[i-1]:
        cnt += arr[i] - K - arr[i-1]
        arr[i-1] = arr[i] - K
print(cnt)