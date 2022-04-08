from itertools import combinations
from collections import Counter

#(solution 1)조합과 딕셔너리 활용

def make_menu(orders, num):
    dict = {}
    for order in orders:
        order = sorted(order) #순서가 다른 경우 방지
        for combi in combinations(order, num): #조합 만들어주기
            key = "".join(combi) #문자열로 key값 만들어주기
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
    return dict

def solution(orders, course):
    result = []

    for num in course:
        dict = make_menu(orders, num)
        if len(dict) == 0:
            continue
        else:
            max_order = max(dict.values()) #가장 많이 주문한 수
            if max_order < 2:
                continue
            else:
                for k, v in dict.items():
                    if v == max_order: #가장 많이 주문한 수와 동일 시 추가
                        result.append(k)

    result.sort()
    return result

#(solution 2)조합과 Counter활용

def make_menu(num, orders):
    pre_menu = []
    for order in orders:
        order = sorted(order)
        for combi in combinations(order, num):
            combi = "".join(combi)
            pre_menu.append(combi)
    menu = Counter(pre_menu).most_common() #가장 많이 있는 수 대로 정렬됨
    return menu

def solution(orders, course):
    result = []
    for num in course:
        menu = make_menu(num, orders)
        if len(menu) > 0 and menu[0][1] >= 2: #메뉴가 공란이 아니고 가장 많이 주문한게 2번이상일 때
            for ans in menu:
                if ans[1] == menu[0][1]: #가장 많이 있는 수와 동일한 경우 추가
                    result.append(ans[0])
    result.sort()
    return result

