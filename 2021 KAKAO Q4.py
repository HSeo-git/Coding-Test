def solution(n, s, a, b, fares):
    #무한대 정의
    INF = int(1e9)

    #2차원 graph만들어주고 무한대로 초기화
    graph = [[INF]*(n+1) for _ in range(n+1)]

    #출발점과 도착점 같은 경우, 0으로 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    #fares 정보 graph에 담아주기
    for i in range(len(fares)):
        graph[fares[i][0]][fares[i][1]] = fares[i][2]
        graph[fares[i][1]][fares[i][0]] = fares[i][2]

    #플로이드워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    #4가지 경우 모두 찾고 min값 반환
    #1번째경우, s->a->b
    case1 = graph[s][a]+graph[a][b]

    #2번째 경우, s->b->a
    case2 =  graph[s][b]+graph[b][a]

    #3번째 경우, s->a, s->b
    case3 = graph[s][a]+graph[s][b]

    #4번째 경우, s->mid, mid->a, mid->b
    case4 = INF
    for mid in range(1, n+1):
        case4 = min(case4, graph[s][mid]+graph[mid][a]+graph[mid][b])

    answer = min(case1, case2, case3, case4)
    return answer