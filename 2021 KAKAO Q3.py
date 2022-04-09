from bisect import bisect_left
from collections import defaultdict
from itertools import product

def solution(info, query):
    applicants = [] #info 데이터 리스트로 가공
    for applicant in info:
        applicants.append(list(applicant.split(" ")))

    conditions = [] #query 데이터 리스트로 가공
    for condition in query:
        condition = list(condition.split(" ")) #score앞에는 and 없어서 split으로 일괄 제외 불가 -> 별도 제외 필요
        cond = (condition[0], condition[2], condition[4], condition[6], condition[7]) #and를 별도 제외
        conditions.append(cond)

    apply_dict = defaultdict(list) #apply정보로 조합 만들어서 dict 생성
    for apply in applicants:
        lan = [apply[0], '-']
        part = [apply[1], '-']
        career = [apply[2], '-']
        food = [apply[3], '-']
        for combi in product(lan, part, career, food, repeat=1):
            apply_dict[combi].append(int(apply[4])) #dict value에는 각 점수 리스트로 넣어주기
    for key in apply_dict:
        apply_dict[key].sort() #value 오름차순 정렬(이분탐색 전제조건)

    ans = [] #query돌면서 dict에서 해당 조건 찾은 다음 점수 체크
    for condi in conditions:
        lan, part, career, food = condi[0], condi[1], condi[2], condi[3]
        score = int(condi[4])
        key = (lan, part, career, food)
        idx = bisect_left(apply_dict[(lan, part, career, food)], score) #이분탐색 이용하여 조건 점수 idx 찾기
        ans.append(len(apply_dict[(key)])-idx) #조건점수 이상 득점 개수 구하여 정답에 추가

    return ans