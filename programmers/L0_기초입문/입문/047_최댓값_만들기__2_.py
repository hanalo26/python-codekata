# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 03. 18:40:56

def solution(numbers):
    new_numbers_list = sorted(numbers)
    
    cal_1 = new_numbers_list[-1] * new_numbers_list[-2]
    
    cal_2 = new_numbers_list[0] * new_numbers_list[1]
    
    return max(cal_1, cal_2) 