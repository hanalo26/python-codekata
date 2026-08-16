# 프로세스
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 08. 16. 18:46:26

from collections import deque

def solution(priorities, location):
    # priorities: 각 위치에 있는 원소들의 중요도(숫자가 클수록 우선순위가 높음)
    # location: priorities의 원소 중 해당 위치에 있는 원소가 실행되는 순서를 최종 반환해야 함
    
    # priorities의 원소별 중요도 (인덱스, 중요도) 형태로 저장
    q = deque(enumerate(priorities))
    
    # 실행된 프로세스
    played = []
    
    # 프로세스 실행 시작!
    while q:
        n_idx, n_primary = q.popleft()
        
        # q가 비어있지 않고, 중요도가 q에 남은 값들의 최댓값보다 n_primary가 작다면 다시 q로 복귀하도록 함
        if q and n_primary < max(p for _,p in q):
            q.append((n_idx, n_primary))
        else: # 프로세스 실행!!!!
            played.append(n_idx)
            # 문제에서 알고싶어하는 위치의 값이 들어갔다면 played의 길이를 반환 = 실행된 순서와 동일
            if n_idx == location:
                return len(played)
    
    return -1