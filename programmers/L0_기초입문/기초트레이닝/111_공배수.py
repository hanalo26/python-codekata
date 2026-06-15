# 공배수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181936
# 알고리즘: 연산
# 작성자: 백하은
# 작성일: 2026. 06. 15. 16:15:01

def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0