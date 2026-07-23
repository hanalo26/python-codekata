# 프로세스
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 07. 23. 23:14:22

from collections import deque

def solution(priorities, location):
    # priorities: 각 원소들의 중요도 점수(높을수록 우선순위가 높음)
    # location: priorities의 원소 중 해당 위치에 있는 원소가 실행되는 순서가 궁금한 것
    
    # priorities의 원소의 고유 번호를 인덱스로 기록+중요도점수
    q = deque(enumerate(priorities)) # [(인덱스, 중요도 점수)] 형태로 저장
    # 실행된 프로세스
    played = []
    
    while q:
        n_idx, n_primary = q.popleft()
        
        # q가 비워져있지 않고, 중요도점수가 q에 남은 것 중 최고점보다 낮다면 다시 q로 복귀
        if q and n_primary < max(p for i, p in q):
            q.append((n_idx, n_primary))
        else:
            played.append(n_idx) # 실행 완료
            if n_idx == location:
                return len(played)
            
    return -1 # 절대 반환되면 안되는 기본 반환값