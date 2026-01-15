# 약수의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 알고리즘: 수학, 반복문
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:46:23

def solution(n):
    answer = 0
    for i in range(1,n+1,1):
        if n % i == 0:
            answer = answer+ i
    return answer