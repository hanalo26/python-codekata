# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 21. 09:31:19

from math import ceil

def solution(slice, n):
    answer = ceil(n/slice)
    return answer