# 나누어 떨어지는 숫자 배열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 알고리즘: 배열, 정렬
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:51:22

def solution(arr, divisor):
    answer = []
    
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    
    #answer이 비어있다면 -1을 추가하고 반환
    if not answer: 
        answer.append(-1)
        return answer
    
    answer.sort()
    return answer

        