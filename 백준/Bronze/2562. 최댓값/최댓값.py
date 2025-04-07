max_idx = 1
max_num = 0
for i in range(1, 10):
    N = int(input())
    if max_num < N:
        max_idx = i
        max_num = N
print(max_num)
print(max_idx)