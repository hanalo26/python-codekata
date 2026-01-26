# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 26. 13:55:07

def solution(n):
    answer = 0
    n_str = str(n)
    for i in n_str:
        answer += int(i)
    return answer