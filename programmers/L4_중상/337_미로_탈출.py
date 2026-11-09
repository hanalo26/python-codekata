# 미로 탈출
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 알고리즘: BFS
# 작성자: 백하은
# 작성일: 2026. 11. 09. 16:30:34

"""
(1) 미로의 구성 요소
    - S: 시작 지점
    - E: 출구
    - L: 레버
    - O: 통로
    - X: 벽 (지나갈 수 없음)

(2) 탈출 및 이동 규칙
    - 한 칸 이동하는 데 1초가 걸림
    - 출구(E)는 레버를 당기기 전에도 지나갈 수 있지만, 반드시 레버(L)를 먼저 당긴 후에 도달해야만 탈출로 인정
    
(3) 구해야 하는 것
    - 시작점(S)에서 레버(L)까지의 가장 짧은 이동 거리 -> 레버(L)에서 출구(E)까지의 가장 짧은 이동 거리 -> 두 이동 거리를 합친 이동 시간을 반환
    - 탈출이 불가능한 경우에는 -1을 반환할 것
"""
from collections import deque

def solution(maps):
    R = len(maps)
    C = len(maps[0])
    
    # 1. 위치 좌표 찾기 (S, L, E)
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)

    # BFS를 이용해 from_pos에서 to_pos까지의 최단 거리를 구하는 함수
    def bfs(from_pos, target_point):
        visited = [[False] * C for _ in range(R)]
        q = deque([(from_pos[0], from_pos[1], 0)]) # (r, c, 거리)
        visited[from_pos[0]][from_pos[1]] = True
        
        # 상하좌우로 이동하기 위한 방향키 역할
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while q:
            r, c, dist = q.popleft()
            
            # 목표 지점에 도달했다면 그동안 걸린 시간(dist) 반환
            if maps[r][c] == target_point:
                return dist
                
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                # 범위를 벗어나지 않고, 벽('X')이 아니며, 아직 방문하지 않은 곳이라면
                if (0 <= nr < R and 0 <= nc < C) and (maps[nr][nc] != 'X') and (not visited[nr][nc]):
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    
        return -1  # 도달할 수 없는 경우

    # 2단계 시뮬레이션
    # 1단계: S -> L 최단 거리
    time_to_lever = bfs(start, 'L')
    if time_to_lever == -1:
        return -1
        
    # 2단계: L -> E 최단 거리
    time_to_exit = bfs(lever, 'E')
    if time_to_exit == -1:
        return -1
        
    # 두 구간의 최단 거리를 합산
    return time_to_lever + time_to_exit