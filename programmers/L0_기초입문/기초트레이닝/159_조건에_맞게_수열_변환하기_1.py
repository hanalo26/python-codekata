# 조건에 맞게 수열 변환하기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181882
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 01. 16. 02:05:11

def solution(arr):
    answer = []
    
    for x in arr:
        if x >= 50 and x % 2 == 0:
            answer.append(x//2)
        elif x < 50 and x % 2 == 1:
            answer.append(x * 2)
        else:
            answer.append(x)
    
    return answer