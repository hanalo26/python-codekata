# 주사위 게임 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181839
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 29. 16:17:27

def solution(a, b):
    if (a % 2 != 0) and (b % 2 != 0):
        return a**2 + b**2
    elif (a % 2 != 0) or (b % 2 != 0):
        return 2*(a+b)
    else:
        return abs(a-b)