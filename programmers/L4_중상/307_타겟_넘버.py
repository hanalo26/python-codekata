# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 18:26:56

from collections import deque

def solution(numbers, target):
    # (누적합, 사용한 숫자의 개수) 조합으로 초기값 정의
    que=deque([(0,0)])
    # 누적합이 target과 같은 조합의 개수
    answer=0
    
    while que:
        # total_sum: 누적합
        # idx: 사용한 숫자의 개수, numbers에서 숫자를 꺼내는 인덱스
        total_sum, idx = que.popleft()
        
        # numbers의 모든 숫자를 다 꺼냈을 때
        if idx == len(numbers):
            # 누적합과 target 비교
            if total_sum == target:
                answer += 1
        
        # numbers의 숫자를 다 꺼내지 못했을 때
        # que의 누적합에 꺼낸 숫자를 더한 경우, 뺀 경우를 모두 추가
        else:
            que.append((total_sum+numbers[idx], idx+1))
            que.append((total_sum-numbers[idx], idx+1))
            
    # 최종 결과
    return answer
            