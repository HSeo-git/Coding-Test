#2020 KAKAO BLIND RECRUITMENT Q.3

#자물쇠에 N-1만큼 padding 주기(열쇠가 이동하는 board생성)
def make_board(padding, M, lock):
    board = [[0]*(M+2*padding) for _ in range(M+2*padding)]
    for i in range(M):
        for j in range(M):
            board[i+padding][j+padding] = lock[i][j]
    return board

#열쇠 돌리기
def rotate_key(key, idx):
    if idx == 0:
        return key
    else:
        new_key = [[0]*(len(key)) for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[j][len(key)-1-i] = key[i][j]
        return new_key

#키 넣기
def put_key(r, c, key, board, lock):
    for i in range(len(key)):
        for j in range(len(key)):
            board[r+i][c+j] += key[i][j]
    return board

#열리는지 확인하기
def is_opened(board, lock, padding):
    for a in range(len(lock)):
        for b in range(len(lock)):
            if board[padding+a][padding+b] != 1:
                return False
    return True

def solution(key, lock):
    M = len(lock)
    N = len(key)
    padding = N - 1

    for r in range(M+padding):
        for c in range(M+padding):
            for i in range(4):
                board = make_board(padding, M, lock)
                key = rotate_key(key, i)
                new_board = put_key(r, c, key, board, lock)
                if is_opened(new_board, lock, padding):
                    return True
    return False