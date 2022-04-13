#2022 KAKAO Q5

def solution(play_time, adv_time, logs):
    #데이터 전처리(초단위로 변환)
    watchers = []
    for log in logs:
        watcher = [int(log[:2])*(60*60)+int(log[3:5])*60+int(log[6:8]), int(log[9:11])*60*60+int(log[12:14])*60+int(log[15:17])]
        watchers.append(watcher)

    play = int(play_time[:2])*(60*60)+int(play_time[3:5])*60+int(play_time[6:8])
    adv = int(adv_time[:2])*(60*60)+int(adv_time[3:5])*60+int(adv_time[6:8])

    #각 시간별 시청자 수 그래프 생성(time point마다 시청자 수 찍어주기)
    graph = [0]*(play+2)
    for watcher in watchers:
        start, end = watcher
        graph[start] += 1
        graph[end] -= 1 #유의사항(종료시각엔 시청이 끝났음, 일반 누적합에서 end+1에 -1을 해주는 것과 상이)

    min_adv_start = min([x[0] for x in watchers])
    max_adv_start = max([x[1] for x in watchers])

    for time in range(min_adv_start-1, max_adv_start+1):
        graph[time] += graph[time-1]

    #누적합 처리(구간합 구하기 용이)
    for time in range(min_adv_start-1, max_adv_start+1):
        graph[time] += graph[time-1]

    #시간 범위 순회하며, 구간합 구하기
    max_watch = 0
    ans = 0
    for time in range(play-adv+1):
        start = time
        adv_end = start+adv
        watch = graph[adv_end-1] - graph[start-1] #종료시각에 시청이 끝났음 반영
        if watch > max_watch:
            max_watch = watch
            ans = start
        else:
            continue

    #답안 형태로 만들어 결과값 반환
    HH = ans//(60*60)
    MM = (ans%(60*60))//60
    SS = (ans%(60*60))%60
    answer = ":".join([str(HH).zfill(2), str(MM).zfill(2), str(SS).zfill(2)])

    return answer