# 문자열 다루기 기본
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:55:27

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False