# 같은 숫자는 싫어
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 작성자: 백하은
# 작성일: 2026. 07. 23. 22:01:37

# 배열의 원소 중 연달아서 같은 숫자가 들어오면 제일 먼저 나온 것만 남기고 나머지는 지운다.

def solution(arr):
    answer = []
    
    for i in arr:
        # answer가 비어 있을 때
        if not answer:
            answer.append(i)
        
        # answer가 비어있지 않을 때
        elif i != answer[-1]:
            answer.append(i)
            
    return answer