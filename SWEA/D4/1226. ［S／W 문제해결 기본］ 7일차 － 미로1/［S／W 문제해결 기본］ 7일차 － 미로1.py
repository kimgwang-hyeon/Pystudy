def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1
     
    while q:
        i,j = q.pop(0)
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if ni < 0 or ni >= 16 or nj < 0 or nj >= 16:
                continue
            if (maze[ni][nj] == 0 or maze[ni][nj] == 3) and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
 
 
 
di = [-1,1,0,0]
dj = [0,0,-1,1]
for tc in range(1,11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    bfs(1,1)
    # for v in visited:
    #     print(v)
    if visited[13][13] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')