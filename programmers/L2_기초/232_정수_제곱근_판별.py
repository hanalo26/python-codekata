# 정수 제곱근 판별
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:48:23

def solution(n):
    x = n ** 0.5 #제곱근 계산
    if x == int(x):
        return (int(x)+1) ** 2
    else: 
        return -1