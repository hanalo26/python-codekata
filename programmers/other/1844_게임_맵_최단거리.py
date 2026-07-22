# 게임 맵 최단거리
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 작성자: 백하은
# 작성일: 2026. 07. 22. 18:06:42

from collections import deque

def solution(maps):
    # 행의 개수
    n = len(maps) # x
    
    # 열의 개수
    m = len(maps[0]) # y
    
    # 이동방향 (상하좌우)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # 시작점 (0,0)
    que = deque([(0,0)])
    
    # 상대팀 진영에 도달하기 위한 최소 이동거리 계산
    while que:
        # 맨 앞에 있는 요소 꺼냄
        x,y = que.popleft()
        
        # 상대팀 진영에 도착했는지 확인
        if (x == n-1) and (y == m-1):
            return maps[x][y]
        
        # 상하좌우로 이동했을 때 이동한 위치의 좌표값
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동한 좌표가 map 내에 있고, 벽(=0)이 아닌지 확인
            if (0 <= nx < n) and (0 <= ny < m) and maps[nx][ny] == 1:
                # maps[nx][ny]에 이동거리 저장
                maps[nx][ny] = maps[x][y] + 1
                # (nx,ny)를 que에 저장 (다음에 이동거리를 또 계산해야 함)
                que.append((nx,ny))
            
    # 끝까지 상대편 진영에 도착하지 못한 경우
    return -1