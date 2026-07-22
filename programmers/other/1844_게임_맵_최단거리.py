# 게임 맵 최단거리
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 작성자: 백하은
# 작성일: 2026. 07. 22. 16:01:51

# BFS(너비 우선 탐색) 방식에 활용되는 내장 라이브러리
from collections import deque

def solution(maps):
    # 행의 개수(n)
    n = len(maps)
    
    # 열의 개수(m)
    m = len(maps[0])
    
    # 이동 패턴 (dx, dy의 같은 인덱스끼리 묶으면 상하좌우 이동 가능)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 초기값 정의 (0, 0)
    que = deque([(0,0)])
    
    while que:
        # 맨 앞에 있는 요소를 꺼냄
        x,y = que.popleft()
        
        # 상대 팀 진영에 도달한 경우
        if x == n-1 and y == m-1:
            return maps[x][y] # 이동거리가 반환됨
        
        # 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # map 내부에 있고, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이동거리를 저장
                maps[nx][ny] = maps[x][y] + 1
                que.append((nx,ny))
                
    # 상대팀 진영에 도착할 수 없는 경우
    return -1