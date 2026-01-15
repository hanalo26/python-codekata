# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:50:26

def solution(a,b):
    smallest_num = min(a,b)
    biggest_num = max(a,b)
    
    num_cnt = biggest_num - smallest_num + 1
    
    total = int((num_cnt * (smallest_num + biggest_num)) / 2)
    
    return total