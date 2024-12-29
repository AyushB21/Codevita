from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

def bfs(board, start, destination, N, M):

    visited = [[False] * M for _ in range(N)]
    queue = deque([(start[0], start[1], 0, 0)]) 
    visited[start[0]][start[1]] = True

    while queue:
        r, c, cells_visited, lifts_used = queue.popleft()
        
        if (r, c) == destination:
            return cells_visited + lifts_used
        
        if board[r][c] == 0:
            while r + 1 < N and board[r + 1][c] == 0:
                r += 1
            if not visited[r][c]:
                visited[r][c] = True
                queue.append((r, c, cells_visited + 1, lifts_used))
        
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
 
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:

                if board[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, cells_visited + 1, lifts_used))

                elif board[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, cells_visited + 1, lifts_used + 1))

    return "Impossible"

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start_row, start_col = map(int, input().split())
destination_row, destination_col = map(int, input().split())

result = bfs(board, (start_row, start_col), (destination_row, destination_col), N, M)

print(result)
