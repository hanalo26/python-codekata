# flag에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181933
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 04. 07. 12:39:49

def solution(a, b, flag):
    if flag == True:
        return a + b
    else:
        return a - b