# 수열과 구간 쿼리 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181924
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 07. 08. 14:28:57

def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr