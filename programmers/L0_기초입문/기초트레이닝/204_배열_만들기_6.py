# 배열 만들기 6
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181859
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 11. 20:08:32

def solution(arr):
    stk = []
    
    for i in arr:
        # stk가 비어있지 않고, 마지막 원소가 현재 값과 같을 때
        if stk and stk[-1] == i:
            stk.pop()
        
        # stk가 비어있거나 마지막 원소가 현재 값과 다를 때
        else:
            stk.append(i)
            
    return stk if stk else [-1]