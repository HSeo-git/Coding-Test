#2020 KAKAO BLIND RECRUITMENT Q.2

#균형잡힌 문자열이 올바른 문자열인지 확인하는 함수
def is_right(word):
    dict = {'(': 1, ')': -1}
    sum = 0
    for w in word:
        sum += dict[w]
        if sum < 0:
            return False
    return True

#균형잡힌 문자열로 나누기 함수(index return)
def slice_word(word):
    dict = {'(': 1, ')': -1}
    sum = 0
    for i in range(len(word)):
        sum += dict[word[i]]
        if sum == 0:
            return i+1
    return len(word)

#u 가공해주기(처음, 마지막 빼고 뒤집어주기)
def make_u(word):
    u = ''
    word = word[1:-1]
    dict_u = {'(':')', ')':'('}
    for w in word:
        u += dict_u[w]
    return u

def dfs(word):
    if len(word) == 0 or is_right(word):
        return word
    else:
        idx = slice_word(word)
        if idx == len(word):
            u = word
            v = ''
        else:
            u = word[:idx]
            v = word[idx:]
        if is_right(u):
            return u+dfs(v)
        else: #u가 옳지 않으면
            result = ''
            result += '('
            result += dfs(v)
            result += ')'
            result += make_u(u)
            return result

def solution(p):
    answer = dfs(p)

    return answer