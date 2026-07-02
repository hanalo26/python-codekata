# n보다 커질 때까지 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181884
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 02. 17:14:10

def solution(numbers, n):
    answer = 0
    
    for num in numbers:
        answer += num
        
        if answer > n:
            return answer
    
    return answer