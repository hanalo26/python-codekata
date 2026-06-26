# 부분 문자열인지 확인하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181843
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 26. 12:12:58

def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0 