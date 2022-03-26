#2020 KAKAO BLIND RECRUITMENT Q.1

def make_div(k, n, s):
    div = []
    for i in range(0, n, k):
        div.append(s[i:i+k])
    return div

def solution(s):
    n = len(s)
    ans = 10**9
    prev = ''
    for k in range(1, n+1):
        str_cnt = 0
        div = make_div(k, n, s)
        for i in range(len(div)):
            if i == 0:
                same_cnt = 1
                prev = div[0]
                str_cnt += len(div[i])
            else: #i가 0이 아닐 때
                if div[i] == prev: #앞의 문자열과 동일할 때
                    same_cnt += 1
                else: #앞의 문자열과 다를 때
                    if same_cnt >= 2:
                        str_cnt += len(str(same_cnt))
                    same_cnt = 1
                    str_cnt += len(div[i])
                    prev = div[i]
        if same_cnt > 1:
            str_cnt += len(str(same_cnt))
        ans = min(ans, str_cnt)

    return ans