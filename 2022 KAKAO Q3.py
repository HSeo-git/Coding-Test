from collections import defaultdict

def solution(fees, records):
    #각 차량 입출차 정보 dict 담기
    car_records = defaultdict(list)
    for record in records:
        clock, car, InOut = list(record.split(' '))
        time = int(clock[:2])*60 + int(clock[3:5])
        car_records[car].append((time, InOut))

    #입출차 정보가 홀수면 23:59출차 정보 추가
    for car in car_records:
        if len(car_records[car]) % 2 > 0:
            car_records[car].append((23*60+59, 'OUT'))

    #Dict 돌면서 누적주차시간 계산하여 list담기
    time_dict = defaultdict(int)
    for car, records in car_records.items():
        for i in range(0, len(records)-1, 2):
            time_dict[car] += (records[i+1][0] - records[i][0])

    #Dict를 차량번호 순으로 정렬
    car_parking = sorted(time_dict.items(), key = lambda x: x[0])

    #차량순으로 돌면서 요금 계산해서 답(리스트)에 담기
    answer = []
    for parking in car_parking:
        time = parking[1]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            if (time-fees[0])%fees[2] == 0:
                ans = fees[1] + ((time-fees[0])//fees[2])*fees[3]
            else:
                ans = fees[1] + (((time-fees[0])//fees[2])+1)*fees[3]
            answer.append(ans)

    return answer