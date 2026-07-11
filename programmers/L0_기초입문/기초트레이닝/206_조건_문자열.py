# 조건 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181934
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 11. 20:17:16

def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        if n >= m:
            return 1
        else:
            return 0
    if ineq == "<" and eq == "=":
        if n <= m:
            return 1
        else:
            return 0
    if ineq == ">" and eq == "!":
        if n > m:
            return 1
        else:
            return 0
    if ineq == "<" and eq == "!":
        if n < m:
            return 1
        else:
            return 0