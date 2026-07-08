# 배열의 길이를 2의 거듭제곱으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181857
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 07. 08. 14:31:46

def solution(arr):
    length = len(arr)
    target_length = 1
    
    while target_length < length:
        target_length = target_length*2
        
    answer = arr + [0] * (target_length-length)
    
    return answer