# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 03. 12:39:43

def solution(n):
    factorial_val = 1
    num = 1
    
    while factorial_val <= n:
        num += 1
        factorial_val = factorial_val * num
    
    return num - 1