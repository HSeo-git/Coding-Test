#2020 KAKAO Q5

#(solution 1) 문제 지시사항 그대로 시뮬레이션 구현

def is_possible_floor(x, y, board_floor, board_pillar, n):
    if x < 0 or x >= n or y <= 0 or y > n: #영역 벗어나면 안됨
        return False
    if y >= 1 and board_pillar[x][y-1] == True: #아래 기둥 조건
        return True
    if y >= 1 and board_pillar[x+1][y-1] == True: #한쪽 끝 기둥 조건(보는 오른쪽으로 설치)
        return True
    if x >= 1 and board_floor[x-1][y] == True and board_floor[x+1][y] == True: #양쪽 보 조건
        return True
    return False


def is_deletable_floor(x, y, board_floor, board_pillar, n): #(보 없는 상태)주변 구조물이 존재했지만 지금 불가능한 경우 거르기
    if board_floor[x+1][y] and not is_possible_floor(x+1, y, board_floor, board_pillar, n): #오른쪽 보
        return False
    if board_pillar[x][y] and not is_possible_pillar(x, y, board_floor, board_pillar, n): #해당 지점 기둥
        return False
    if board_pillar[x+1][y] and not is_possible_pillar(x+1, y, board_floor, board_pillar, n): #오른쪽 기둥
        return False
    if x >= 1 and board_floor[x-1][y] and not is_possible_floor(x-1, y, board_floor, board_pillar, n): #왼쪽 보
        return False
    return True


def is_possible_pillar(x, y, board_floor, board_pillar, n):
    if x < 0 or x > n or y >= n or y < 0: #영역 벗어나면 안됨
        return False
    if y == 0: #바닥인 경우
        return True
    if board_floor[x][y] == True or (x >= 1 and board_floor[x-1][y]) == True: #아래에 보의 한쪽 끝
        return True
    if y >= 1 and board_pillar[x][y-1] == True: #아래에 기둥
        return True
    return False


def is_deletable_pillar(x, y, board_floor, board_pillar, n): #(기둥 없는 상태)주변 구조물이 존재했지만 지금 불가능한 경우 거르기
    if board_pillar[x][y+1] and not is_possible_pillar(x, y+1, board_floor, board_pillar, n): #위쪽 기둥
        return False
    if board_floor[x][y+1] and not is_possible_floor(x, y+1, board_floor, board_pillar, n): #위쪽 바닥
        return False
    if x >= 1 and board_floor[x-1][y+1] and not is_possible_floor(x-1, y+1, board_floor, board_pillar, n): #왼위 바닥
    return True


def solution(n, build_frame):
    # 보와 기둥의 board를 padding을 넉넉히 주고 만들어주기(False: 없음, True: 있음)
    board_floor = [[False] * (n*2) for _ in range(n*2)]
    board_pillar = [[False] * (n*2) for _ in range(n*2)]

    for command in build_frame:
        x, y, a, b = command
        if a == 1:  # 보일 때
            if b == 0:  # 삭제
                if board_floor[x][y]:  # 보가 있을 때
                    board_floor[x][y] = False #해당 보 없애주기
                    if not is_deletable_floor(x, y, board_floor, board_pillar, n):  # 보 없이도 주변 구조물이 만족하는지
                        board_floor[x][y] = True #주변 구조물이 만족하지 않는다면, 다시 살려주기
            else:  # 설치
                if not board_floor[x][y]:
                    if is_possible_floor(x, y, board_floor, board_pillar, n):  # 해당 보가 있을 수 있는지
                        board_floor[x][y] = True
        else:  # 기둥일 때
            if b == 0:  # 삭제
                if board_pillar[x][y]:  # 기둥이 있을 때
                    board_pillar[x][y] = False #기둥 없애주기
                    if not is_deletable_pillar(x, y, board_floor, board_pillar, n): #기둥 없이도 주변 구조물 만족하는지
                        board_pillar[x][y] = True #주변 구조물이 만족하지 않는다면, 다시 살려주기
            else:  # 설치
                if not board_pillar[x][y]:
                    if is_possible_pillar(x, y, board_floor, board_pillar, n):
                        board_pillar[x][y] = True

    #x, y, 기둥, 보 순으로 정렬하여 답안작성
    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if board_pillar[x][y]:
                answer.append([x, y, 0])
            if board_floor[x][y]:
                answer.append([x, y, 1])

    return answer

#(solution 2) 구조물을 설치/삭제 시, 전체구조물이 성립가능한지 체크

def is_possible(answer):
    for ans in answer:
        x, y, a = ans
        if a == 1:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
        else:  # 기둥
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for command in build_frame:
        x, y, a, b = command
        if b == 1:  # 설치
            answer.append([x, y, a]) #먼저 설치해주기
            if not is_possible(answer): #전체 구조물 가능한지 체크
                answer.remove([x, y, a]) #불가능하면 다시 원복
        else:  # 삭제
            if [x, y, a] in answer:
                answer.remove([x, y, a]) #먼저 삭제해주기
                if not is_possible(answer): #전체 구조물 가능한지 체크
                    answer.append([x, y, a]) #불가능하면 다시 원복

    answer.sort()

    return answer