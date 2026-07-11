# 배열 만들기 4
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181918
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 07. 11. 20:28:10

def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
            
        elif arr[i] > stk[-1]:
            stk.append(arr[i])
            i += 1
        else:
            # stk 문자열의 마지막 원소가 현재보다 크거나 같을 때 탈락되는 경우
            stk.pop()
            
    return stk