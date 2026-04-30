# 외계어 사전
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120869
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 30. 10:09:27

def solution(spell, dic):
    # spell의 알파벳을 오름차순 정렬
    target = sorted(spell)
    
    # 사전에 있는 단어도 알파벳 오름차순 정렬했을 때,
    #  target과 동일하다면 1를 반환하고 없으면 2를 반환
    for word in dic:
        if sorted(word) == target:
            return 1
        
    return 2