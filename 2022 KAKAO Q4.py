from itertools import combinations_with_replacement

def solution(n, info):
    max_score = 0
    answer = [0] * (len(info))
    #라이언의 샷 조합(중복조합)
    for combi in combinations_with_replacement(range(11), n):
        lion_shots = [0] * (len(info))
        score = 0 #점수차이
        for c in combi:
            lion_shots[10-c] += 1
        for i in range(len(info)): #과녁 돌면서 점수차이 구하기
            if lion_shots[i] > info[i]:
                score += (10-i)
            elif info[i] != 0:
                score -= (10-i)
        if score > max_score: #max_score보다 클 때만 갱신
            max_score = score
            answer = lion_shots

    if max_score > 0:
        return answer
    else: return [-1] #max_score가 여전히 0이면 라이언이 이길 수 없다는 뜻