# 내적
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 알고리즘: 배열, 수학
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:53:52

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer