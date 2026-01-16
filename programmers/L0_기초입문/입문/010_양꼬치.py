# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 16. 17:49:37

def solution(n, k):
    meat = 12000 * n
    drink = 2000 * (k - (n // 10))
    total = meat + drink
    return total