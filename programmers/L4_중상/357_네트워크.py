# 네트워크
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 07. 22. 16:41:59

from collections import deque

def solution(n, computers):
    # 초기값
    # 모든 컴퓨터가 네트워크에 연결되어 있지 않은 상황
    coms = [False] * n
    
    # 네트워크의 개수
    answer = 0
    
    # 컴퓨터 번호별로 연결된 네트워크 확인
    for idx in range(n):
        # 아직 연결하지 않은 컴퓨터 발견!
        if not coms[idx]:
            answer += 1
            que = deque([idx])
            coms[idx] = True
        
        # 이 컴퓨터와 연결된 모든 컴퓨터 확인
        while que:
            com = que.popleft()
            
            for next_com in range(n):
                # 연결된 컴퓨터이지만 아직 확인하지 않은 경우 
                if computers[com][next_com] == 1 and not coms[next_com]:
                    coms[next_com] = True
                    que.append(next_com)
                    
    return answer