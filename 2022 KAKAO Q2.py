import math

# 진법변환 함수
def convert(n, base):
    tmp = ''
    while n:
        tmp += str(n % base)
        n = n // base
    return tmp[::-1]


# 소수판별 함수
def is_Prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    new_n = convert(n, k)
    P_list = list(new_n.split('0')) #0을 기준으로 나눠주기

    cnt = 0
    for P in P_list:
        if P != '': #공란 예외처리
            if is_Prime(int(P)): #소수일 때 cnt 증가
                cnt += 1
    return cnt



