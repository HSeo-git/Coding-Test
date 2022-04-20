from collections import defaultdict

# 정답 초기값 설정
max_sheep = 0

# dfs로 최대 양 개수 찾아주기
def find_sheep(node, info, visited, sheep, wolf, next_list, children_dict):
    global max_sheep
    SHEEP = 0
    WOLF = 1
    if info[node] == SHEEP:
        sheep += 1
        max_sheep = max(sheep, max_sheep)
    elif info[node] == WOLF:
        wolf += 1
    if wolf >= sheep:
        return
    visited[node] = True
    if children_dict[node]:
        next_list += children_dict[node]
    for next in next_list:
        find_sheep(next, info, visited[:], sheep, wolf, [n for n in next_list if n != next and not visited[n]],
                   children_dict)

def solution(info, edges):
    # children dict생성
    children_dict = defaultdict(list)  # key:부모, value:자식
    for edge in edges:
        parent, children = edge
        children_dict[parent].append(children)
    # visited 초기값 생성
    visited = [False] * len(info)
    #dfs 실행
    find_sheep(0, info, visited, 0, 0, [], children_dict)

    return max_sheep
