# 전력망을 둘로 나누기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 알고리즘: DFS/BFS, 그래프
# 작성자: 백하은
# 작성일: 2026. 10. 26. 19:00:27

from collections import deque

# 서브 - 각 전력망에 연결된 송전탑의 개수 반환
# s: 송전탑의 번호(시작점)
# mapd : 각각의 송전탑이 연결된 송전탑을 표시한 지도
# cut_a,b : 전선 연결이 끊어진 두 송전탑의 번호 
def cnt_nodes(s,n,mapd, cut_a, cut_b):
    visited = [False]*(n+1)
    
    visited[s] = True # 시작점
    
    # 어느 한 전력망에 연결된 송전탑의 개수
    cnt = 1
    
    # 다음에 탐색할 송전탑
    q = deque([s])
    
    # 탐색
    while q:
        # 현재 서있는 송전탑(기준)
        cur = q.popleft()
        
        # 기준과 연결된 송전탑
        for nxt in mapd[cur]:
            # 혹시 cur-nxt 전선이 끊어진 전선이면 건너뛰어야 함
            if (cur == cut_a and nxt == cut_b) or (nxt == cut_a and cur == cut_b):
                continue
            
            # 위 조건을 통과하고, 카운트하지 않은 송전탑이라면
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
                
    return cnt
    

# 메인 - 지도를 그리면서 각 전력망 별로 연결된 송전망 개수의 차이 반환
def solution(n, wires):
    # mapd 정의
    mapd = [[] for _ in range(n+1)]
    
    # 전선으로 연결된 송전탑
    for v1, v2 in wires:
        mapd[v1].append(v2)
        mapd[v2].append(v1)
    
    # 두 전력망에 연결된 송전탑의 개수 차이
    # 초기에는 전체 송전탑 개수로 설정 - 전부 연결되어 있지 않은 상황을 가정
    answer = n
    
    # wires에 있는 전선을 순차적으로 cutting
    for v1, v2 in wires:
        # v1이 속한 전력망에 연결된 송전탑의 개수
        cnt1 = cnt_nodes(v1,n,mapd,v1, v2)
        
        # v2가 속한 전력망에 연결된 송전탑의 개수
        cnt2 = n - cnt1
        
        # 두 값의 차이
        diff = abs(cnt1-cnt2)
        
        # answer 갱신
        answer = min(answer, diff)
        
    return answer