#2020 KAKAO BLIND RECRUITMENT Q.3

from collections import deque

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

#자물쇠에 N-1만큼 padding 주기(열쇠가 이동하는 board생성)
M = len(lock)
N = len(key)
board = [[0]*(M+N-1) for _ in range(M+N-1)]
for i in range(M):
    for j in range(M):
        board[i+N-1][j+N-1] = lock[i][j]

#열쇠이동
def bfs(board, key, N, M):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q = deque()
    q.append([0,0])
    while q:
        y, x = q.popleft()
        if is_openable(board, y, x, N, M, key):
            return True
        else:
            new_key = rotated_key(key, N)
            if is_openable(board, y, x, N, M, new_key):
                return True
        for k in range(4):
            next_y = y+dy[k]
            next_x = x+dx[k]
            if next_y >= (M+N-1) or next_x >= (M+N-1) or next_y < 0 or next_x < 0:
                continue
            q.append([next_y, next_x])
    return False

#열쇠회전
def rotated_key(key, N):
    new_key = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_key[j][N-i-1] = key[i][j]
    return new_key

#자물쇠 열리는지 확인
def is_openable(board, y, x, N, M, key):
    for i in range(N):
        for j in range(N):
            board[i + y][j + x] += key[i][j]
    for a in range(1, M):
        for b in range(1, M):
            board[a + N -1][b + N -1] += board[a + N -1-1][b + N -1-1]
    for c in range(1, M):
        board[c][M-1] += board[c-1][M-1]
    if board[M-1][M-1] == M*M:
        return True
    return False

if bfs(board, key, N, M):
    print(True)
else: print(False)