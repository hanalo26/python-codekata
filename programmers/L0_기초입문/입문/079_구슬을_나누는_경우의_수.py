# 구슬을 나누는 경우의 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 26. 16:16:41

import math

# 조합(nCr) : comb(n, r)

def solution(balls, share):
    answer = math.comb(balls, share)
    return answer