import sys

lines = sys.stdin.readlines()
N, target, P = map(int, lines[0].strip().split())
if len(lines) == 2:
    data = list(map(int, lines[1].strip().split()))
else:
    data = []


result = 1
count = 1

for score in data:
    if count > P:
        break
    if score > target:
        result += 1
        count += 1
    elif score == target:
        count += 1
    else:
        break

if count > P:
    print(-1)
else:
    print(result)
