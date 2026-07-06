# 마지막 두 원소
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181927
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 06. 14:53:04

def solution(num_list):
    last = num_list[-1]
    prev = num_list[-2]
    
    # 조건에 따라 마지막 원소 추가
    if last > prev:
        num_list.append(last-prev)
    else:
        num_list.append(last*2)
    
    return num_list