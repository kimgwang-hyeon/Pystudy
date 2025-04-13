def iron_bar(arrangement):
    stack = []
    total_pieces = 0

    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:  # ')'
            stack.pop()
            if arrangement[i - 1] == '(':
                total_pieces += len(stack)
            else:
                total_pieces += 1

    return total_pieces

arr = input().strip()
print(iron_bar(arr))
