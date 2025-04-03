from collections import Counter


N = int(input())
sum_arr = 0
arr = []
set_arr = set()
diction = dict
for i in range(N):
    x = int(input())
    sum_arr += x
    arr.append(x)
arr.sort()
print(round(sum_arr/N))
print(arr[(N-1)//2])
counter = Counter(arr)
most_common = counter.most_common()
max_count = most_common[0][1]

# 최빈값들만 필터링
modes = [val for val, cnt in most_common if cnt == max_count]

if len(modes) == 1:
    print(modes[0])  # 최빈값이 1개뿐이면 그 값 반환
else:
    modes.sort()
    print(modes[1])  # 두 번째로 작은 값 반환
print(arr[-1] - arr[0])