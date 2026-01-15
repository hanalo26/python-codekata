# 제일 작은 수 제거하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 알고리즘: 배열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:53:14

def solution(arr):
    answer = []
    min_value = min(arr)
    
    if len(arr) == 1:
        return [-1]
    else:
        for num in arr:
            if num > min_value:
                answer.append(num)
    
        return answer