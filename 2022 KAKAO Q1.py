from collections import defaultdict

def solution(id_list, report, k):
    #전처리 : 동일 유저 중복신고 처리
    new_report = set(report)

    #new_report 돌면서 신고내용 dict화
    #(dict) key 이용자: value 신고한 유저리스트
    report_dict = defaultdict(list)
    for re in new_report:
        reporter, target = re.split(" ")
        report_dict[target].append(reporter)

    #안내메일 받을 이용자 정리
    #(dict) key 이용자: value 안내메일 횟수
    mail_dict = {}
    for id in id_list:
        mail_dict[id] = 0
    #report_dict돌면서 대상자 확인 후, mail_dict에 안내 횟수 넣어주기
    for result in report_dict.values():
        if len(result) >= k:
            for v in result:
                mail_dict[v] += 1
        else:
            continue

    answer = list(mail_dict.values())
    return answer