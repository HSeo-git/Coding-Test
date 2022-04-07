#2021 KAKAO Q1

#1단계(소문자 변경)
def step1(new_id):
    new_id = new_id.lower()
    return new_id
#2단계(가능한 문자만 남기기)
def step2(new_id):
    ans = ''
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in ['-', '_', '.']:
            ans += char
        else: continue
    return ans
#3단계(..을 .으로 바꿔주기)
def step3(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id
#4단계(.가 앞이나 끝에 붙지 않도록)
def step4(new_id):
    if len(new_id) == 0:
        return ''
    while new_id[0] == '.':
        new_id = new_id[1:]
        if len(new_id) == 0:
            return ''
    while new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
        if len(new_id) == 0:
            return ''
    return new_id
#5단계(빈 문자열이면 'a'반환)
def step5(new_id):
    if len(new_id) == 0:
        return 'a'
    else: return new_id
#6단계(길이가 15 이하가 되도록, 슬라이싱 후 .가 마지막이면 제거)
def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    return new_id
#7단계(길이가 2이하이면 길이가 3이 될때까지 마지막 문자 더하기)
def step7(new_id):
    if len(new_id) <= 2:
        new_id  = new_id + new_id[-1]*(3-len(new_id))
    return new_id

def solution(new_id): #단계별로 실행
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id