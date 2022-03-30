#2020 KAKAO Q4

#(solution 1) 이분탐색 사용

from bisect import bisect_left, bisect_right
from collections import defaultdict


# 이분탐색 사용
# 배열에서 특정 값 구간의 원소 개수 반환 함수
def find_range(array, left, right):
    left_idx = bisect_left(array, left)
    right_idx = bisect_right(array, right)
    return right_idx - left_idx


def solution(words, queries):
    # 길이 별로 word를 담을 dict.를 쌍(origin., reversed)으로 생성
    # 두 dict. value들 sort(이분탐색 전제조건)
    dic = defaultdict(list)
    re_dic = defaultdict(list)
    for word in words:
        dic[len(word)].append(word)
        re_dic[len(word)].append(word[::-1])
    for i in range((10 ** 4) + 1):
        if dic[i]:
            dic[i].sort()
            re_dic[i].sort()

    # queires를 순회하며 query길이에 맞는 dic value에서 값 찾기
    answer = []
    ans = 0
    for query in queries:
        if query[0] != '?':
            ans = find_range(dic[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
            answer.append(ans)
        else:
            re_query = query[::-1]
            ans = find_range(re_dic[len(query)], re_query.replace('?', 'a'), re_query.replace('?', 'z'))
            answer.append(ans)

    return answer

#(solution 2) Trie 자료구조 활용

#Node 설정
#개수를 쉽게 셀 수 있도록 cnt 매개변수 추가
class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.cnt = 0

#Trie 자료구조 설정(insert, search)
class Trie:
    def __init__(self):
        self.root = Node(None)
    def insert(self, word):
        curr = self.root
        for w in word:
            curr.cnt += 1
            if w not in curr.children:
                curr.children[w] = Node(w)
            curr = curr.children[w]
        curr.cnt += 1
    def search(self, query):
        curr = self.root
        for q in query:
            if q == '?':
                return curr.cnt
            elif q in curr.children:
                curr = curr.children[q]
            else: return 0
        return curr.cnt

def solution(words, queries):

    #origin. dict와 reversed dict 생성
    trie = dict()
    re_trie = dict()

    #words 돌면서 dict에 word len별로 Trie() 구조 추가
    for word in words:
        trie[len(word)] = Trie()
        re_trie[len(word)] = Trie()
    #각 trie dict의 해당 len의 Trie구조에 word를 insert(reversed에는 거꾸로 insert)
    for word in words:
        trie[len(word)].insert(word)
        re_trie[len(word)].insert(word[::-1])

    result = []
    #queries를 돌면서 query길이 별로 해당되는 Trie구조에서 search 수행
    #query의 길이가 아예 없는 경우 예외처리 필요
    for query in queries:
        if len(query) not in trie:
            res = 0
        elif query[0] != '?':
            res = trie[len(query)].search(query)
        else:
            res = re_trie[len(query)].search(query[::-1])
        result.append(res)

    return result










