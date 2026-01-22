# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 22. 14:17:37

def solution(n):
    root = n ** 0.5
    if root.is_integer():
        return 1
    else:
        return 2