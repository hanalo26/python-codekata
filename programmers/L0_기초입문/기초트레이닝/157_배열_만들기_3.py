# 배열 만들기 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181895
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 01. 14:45:36

def solution(arr, intervals):
    
    # 구간 분리
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    
    # 구간별 원소 꺼내기
    first = arr[a1:b1+1]
    second = arr[a2:b2+1]    
    
    return first+second