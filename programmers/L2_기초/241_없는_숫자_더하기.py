# 없는 숫자 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 알고리즘: 배열, 해시
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:52:59

def solution(numbers):
    none_number_sum = 0
    
    for i in range(0,10):
        if i not in numbers:
            none_number_sum += i
    
    return none_number_sum