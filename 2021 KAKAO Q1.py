#1단계
def step1(new_id):
    new_id = new_id.lower()
    return new_id
#2단계
def step2(new_id):
    ans = ''
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in ['-', '_', '.']:
            ans += char
        else: continue
    return ans
#3단계
def step3(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id
#4단계
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
#5단계
def step5(new_id):
    if len(new_id) == 0:
        return 'a'
    else: return new_id
#6단계
def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    return new_id
#7단계
def step7(new_id):
    if len(new_id) <= 2:
        new_id  = new_id + new_id[-1]*(3-len(new_id))
    return new_id

def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id