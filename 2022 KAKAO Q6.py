#누적합을 계산해주기 위해 기본값 찍는 별도 함수
def do_skill(new_board, type, r1, c1, r2, c2, degree):
    if type == 1: #공격
        degree = -degree
    new_board[r1+1][c1+1] += degree
    new_board[r1+1][c2+1+1] -= degree
    new_board[r2+1+1][c1+1] -= degree
    new_board[r2+1+1][c2+1+1] += degree

def solution(board, skill):
    #누적합 계산할 별도 board 생성(dp위한 padding 설정)
    new_board = [[0] * (len(board[0]) + 2) for _ in range(len(board) + 2)]

    #skill 돌면서 new_board에 누적합 기본값 찍어주기
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        do_skill(new_board, type, r1, c1, r2, c2, degree)

    #행/열 기준 누적합 계산
    for i in range(1, len(new_board)):
        for j in range(len(new_board[0])):
            new_board[i][j] += new_board[i-1][j]
    for j in range(1, len(new_board[0])):
        for i in range(len(new_board)):
            new_board[i][j] += new_board[i][j-1]

    #board에 누적합 결과 반영
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += new_board[i+1][j+1]

    #board 돌면서 내구도 0 초과 건물 카운트
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1

    return cnt