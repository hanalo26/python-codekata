# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 28. 09:54:14

def solution(array):
    array.sort()
    mid_index = len(array)//2
    
    return array[mid_index]
