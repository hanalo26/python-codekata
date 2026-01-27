# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 27. 09:27:42

def solution(numbers):
    answer = []
    
    for num in numbers:
        answer.append(num * 2)
    
    return answer