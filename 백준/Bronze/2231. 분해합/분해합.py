def find_constructor(N):
    start = max(1, N - 9 * len(str(N)))
    for M in range(start, N):
        if M + sum(int(d) for d in str(M)) == N:
            return M
    return 0


N = int(input())
print(find_constructor(N))

