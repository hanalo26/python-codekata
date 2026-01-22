# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 22. 10:26:33

def solution(s1, s2):
    answer = 0
    
    for item_1 in s1:
        if item_1 in s2:
            answer += 1
    
    return answer