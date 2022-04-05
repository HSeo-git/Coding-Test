from collections import deque

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = 7

def find_next_step(new_board, A, B):
    next_steps = [] #다음 이동가능한 칸을 담을 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    a_r, a_c = A
    b_r, b_c = B
    for i in range(4): #상/하/좌/우 이동
        n_a_r = a_r + dr[i]
        n_a_c = a_c + dc[i]
        n_b_r = b_r + dr[i]
        n_b_c = b_c + dc[i]
        if new_board[n_a_r][n_a_c] == 0 and new_board[n_b_r][n_b_c] == 0:
            next_steps.append({(n_a_r, n_a_c), (n_b_r, n_b_c)})
    if a_r == b_r: #회전(가로로 위치할 때)
        if new_board[a_r+1][a_c] == 0 and new_board[b_r+1][b_c] == 0:
            next_steps.append({(a_r, a_c), (a_r+1, a_c)})
            next_steps.append({(b_r+1, b_c), (b_r, b_c)})
        if new_board[a_r-1][a_c] == 0 and new_board[b_r-1][b_c] == 0:
            next_steps.append({(a_r, a_c), (a_r-1, a_c)})
            next_steps.append({(b_r-1, b_c), (b_r, b_c)})
    if a_c == b_c: #회전(세로로 위치할 때)
        if new_board[a_r][a_c+1] == 0 and new_board[b_r][b_c+1] == 0:
            next_steps.append({(a_r, a_c), (a_r, a_c+1)})
            next_steps.append({(b_r, b_c+1), (b_r, b_c)})
        if new_board[a_r][a_c-1] == 0 and new_board[b_r][b_c-1] == 0:
            next_steps.append({(a_r, a_c-1), (a_r, a_c)})
            next_steps.append({(b_r, b_c-1), (b_r, b_c)})
    return next_steps #다음 이동가능한 칸 리스트 반환

n = len(board)

new_board = [[1]*(n+2) for _ in range(n+2)] #board에 padding주기(board밖 나가는 것 관리용이)
for i in range(n):
    for j in range(n):
        new_board[i+1][j+1] = board[i][j]

visited = [] #방문관리(칸 두개의 집합으로 관리)

q = deque() #bfs 방식 풀이적용
q.append(({(1, 1), (1, 2)}, 0))
visited.append({(1, 1), (1, 2)})

while q:
    curr, cost = q.popleft()
    A, B = curr
    if A == (n, n) or B == (n, n): #둘 중 하나가 목적지 도착하면 cost 반환
        return cost
    else:
        next_steps = find_next_step(new_board, A, B)
        for step in next_steps:
            if step not in visited: #이동가능한 칸 중에서 미방문칸만 이동
                visited.append(step)
                q.append((step, cost+1))
return False