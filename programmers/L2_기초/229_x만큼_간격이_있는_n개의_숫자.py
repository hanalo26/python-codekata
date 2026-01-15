# x만큼 간격이 있는 n개의 숫자
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 알고리즘: 배열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:47:12

def solution(x, n):
    result = []
    for i in range(1,n+1):
        result.append(i*x)
    return result