# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 22. 14:00:41

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
            