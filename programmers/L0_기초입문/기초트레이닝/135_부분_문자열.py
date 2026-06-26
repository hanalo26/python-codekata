# 부분 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181842
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 26. 12:03:37

def solution(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0