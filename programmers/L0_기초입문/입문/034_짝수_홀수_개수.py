# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 23. 09:34:31

def solution(num_list):
    even_count = 0  # 짝수의 개수
    odd_count = 0  # 홀수의 개수
    
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return [even_count,odd_count]