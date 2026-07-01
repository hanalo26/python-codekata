# 가까운 1 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181898
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 01. 14:38:44

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
        
    return -1