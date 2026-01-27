# 중복된 숫자 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 27. 09:30:16

def solution(array, n):
    count = 0
    
    for i in array:
        if i == n:
            count += 1
    
    return count