# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 19. 20:35:03

def solution(n, t):
    # 증식한 세균의 수 = (처음 존재하던 세균의 마리수) * 2^(경과된 시간)
    return n * (2 ** t)