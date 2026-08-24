# 뒤에 있는 큰 수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 알고리즘: 스택
# 작성자: 백하은
# 작성일: 2026. 08. 24. 18:28:34

def solution(numbers):
    # numbers의 길이
    n = len(numbers)
    
    # 뒷 큰수를 못 찾는 경우를 기본값으로 설정한 정답 배열
    answer = [-1] * n
    
    # 아직 튁 큰수를 못 찾은 숫자들의 모임
    stack = []
    
    for i in range(n):
        # stack이 비어있지 않고, 현재 숫자가 스택의 맨 뒤 숫자(=인덱스) 위치에 있는 숫자보다 크다면 뒷 큰수 찾기 성공
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
            
        # 사용했던 인덱스 저장
        stack.append(i)
    
    return answer