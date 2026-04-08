# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 08. 09:46:43

def solution(n):
    answer = []
    d = 2
    
    while d <= n:
        if n % d == 0:
            if d not in answer:
                answer.append(d)
            n = n // d
        else:
            d += 1
    
    return answer