# 짝수와 홀수
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12937
# 알고리즘: 기본연산, 조건문
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:43:57

def solution(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'