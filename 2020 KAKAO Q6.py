from bisect import bisect_left
from itertools import permutations

# 각 지점에서 출발할 수 있도록 circle 연장해주기
circle = weak + [w+n for w in weak]

#min값으로 업데이트할 수 있도록 초기값 설정
INF = int(1e9)
answer = INF

for i in range(len(weak)):
    new_circle = circle[i:i + len(weak)] #각 출발점을 기준으로 점검할 새로운 circle 생성
    for friends in permutations(dist, len(dist)): #점검 보낼 친구들 조합
        cnt = 0 #점검 친구 수 초기화
        idx = 0 #친구별로 점검 시작할 곳 index 초기화
        for friend in friends: #친구 조합 돌면서 점검 시작
            cnt += 1
            visit = new_circle[idx] + friend #시작점으로부터 친구가 갈 수 있는 거리
            if visit >= new_circle[-1]: #circle의 마지막까지 찍으면 answer 업데이트
                answer = min(answer, cnt)
                break
            else:
                idx = bisect_left(new_circle, visit) #마지막 도달하지 못했으면 다음 출발점 idx 돌려주기
                if new_circle[idx] == visit: #visit과 idx가 같을 경우(visit 지점부터 출발하게됨) 예외처리
                    idx += 1

if answer == INF:
    return -1
else: return answer