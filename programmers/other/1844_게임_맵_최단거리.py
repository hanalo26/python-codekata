# 게임 맵 최단거리
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 작성자: 백하은
# 작성일: 2026. 07. 24. 14:14:15

from collections import deque

def solution(maps):
    # 맵의 크기
    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    # 시작점 (0,0)
    q = deque([(0,0)])
    
    # 방향키 (상하좌우)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    # 탐색
    while q:
        r,c = q.popleft()
        
        # 도착지에 도달했는지 확인
        if r == n-1 and c == m-1:
            return maps[r][c]
        
        # 도착하지 못한 경우
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # map 내에 있고, 벽에 부딪히진 않았는지 확인
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                q.append((nr,nc))
                
    # 끝까지 도달하지 못한 경우
    return -1