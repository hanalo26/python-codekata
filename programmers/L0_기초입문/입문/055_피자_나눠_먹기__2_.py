# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 11. 09:47:46


def solution(n):
    pizza = 1
    
    while (pizza * 6) % n != 0:
        pizza += 1
    
    return pizza