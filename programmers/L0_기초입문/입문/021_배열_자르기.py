# 배열 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120833
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 21. 09:28:10

def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer