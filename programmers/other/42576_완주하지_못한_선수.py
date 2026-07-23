# 완주하지 못한 선수
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 작성자: 백하은
# 작성일: 2026. 07. 23. 20:03:31

from collections import Counter

def solution(participant, completion):
    # 딕셔너리처럼 만들어서 각 요소가 각 리스트에서 몇번 등장하는지 확인
    p = Counter(participant)
    c = Counter(completion)
    
    # {'이름'; 등장횟수}
    answer = p - c
    
    # answer에는 등장횟수가 1 이상인 명단만 나옴
    return "".join(list(answer)[0])