# 네트워크
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 07. 24. 14:56:22

from collections import deque

def solution(n, computers):
    # 네트워크 개수 (함수를 통해 구해야 하는 값!)
    answer = 0
    
    #0번부터 n-1번 컴퓨터까지 중 확인한 컴퓨터 목록(같은 번호의 컴퓨터를 2번 확인하지 않기 위해서 체크)
    visited = [False] * n
    
    # 컴퓨터 번호별 연결된 컴퓨터 확인
    for num in range(n):
        # 동일한 번호의 컴퓨터는 같은 네트워크에 연결된 것
        if not visited[num]:
            answer += 1
            visited[num] = True
            
            q = deque([num])
            
            # num번째 컴퓨터와 다른 컴퓨터와의 연결 확인
            while q:
                com = q.popleft()
                
                for other in range(n):
                    if computers[com][other] == 1 and not visited[other]:
                        visited[other] = True
                        q.append(other)
    return answer