T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    case_num = arr[0]
    students = arr[1:]

    line = []
    moves = 0

    for student in students:
        pos = 0
        while pos < len(line) and line[pos] < student:
            pos += 1
        moves += len(line) - pos
        line.insert(pos, student)

    print(case_num, moves)
