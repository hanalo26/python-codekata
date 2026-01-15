# 자릿수 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 알고리즘: 문자열, 반복문
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:45:51

def solution(n):
    answer = 0
    list=str(n)
    for a in range(len(list)):
        b = int(list[a])
        answer = answer + b

    return answer