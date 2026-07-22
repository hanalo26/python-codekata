# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 16:23:35

from collections import deque

def solution(numbers, target):
    # (누적합, 현재까지 사용한 숫자의 개수(=인덱스))
    que = deque([(0,0)]) # 초기값
    answer = 0 # target 숫자가 나오도록 하는 방법의 개수
    
    while que:
        total_sum, idx = que.popleft()
        
        # 모든 숫자를 꺼내 사용한 경우
        if idx == len(numbers):
            if total_sum == target:
                answer += 1
        
        # 아직 숫자를 다 꺼내지 못한 경우
        else:
            # 꺼낸 숫자를 더하는 경우
            que.append((total_sum + numbers[idx], idx+1))
            
            # 꺼낸 숫자를 빼는 경우
            que.append((total_sum - numbers[idx], idx+1))
            
    return answer