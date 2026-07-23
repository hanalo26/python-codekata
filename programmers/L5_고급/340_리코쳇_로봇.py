# 리코쳇 로봇
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 알고리즘: BFS
# 작성자: 백하은
# 작성일: 2026. 07. 23. 12:46:05

# 문제 조건
# - 로봇은 어느 한 방향으로 이동하되, 벽이나 장애물에 부딪힐 때까지 미끄러져서 이동함
# - 목표지점에 도착하지 위해서는 몇 번 미끄러져야 할까??!!
# == 구해야 하는 것: 목표 위치에 도달하기 위해 미끄러져야 하는 횟수
#     단, 도달할 수 없다면 -1을 return
# - "."은 빈 공간
# - "R"은 로봇의 처음 위치
# - "D"는 장애물의 위치 = 로봇의 이동이 멈춰야 함
# - "G"는 목표지점

# 필요한 것: 격자의 크기, 상하좌우 이동을 위한 방향키, R과 G의 좌표, 이동횟수 count, 
from collections import deque

def solution(board):
    # 1.격자의 크기
    n = len(board) # x (행)
    m = len(board[0]) # y (열)
    
    # 2.시작점과 목표지점 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j) # 시작점
            elif board[i][j] == "G":
                end = (i,j) # 목표지점
    
    # 3.방향키 설정
    directions = [
        (-1,0), # 상
        (1,0), # 하
        (0,-1), # 좌
        (0,1)  # 우
    ]
    
    # 4.탐색을 위한 준비
    # (1) 이미 멈춰본 칸들의 모음
    # 중복을 자동으로 제거하기 위해 집합으로 선언
    visited = {start}
    
    # (2) 조사해야 하는 칸들의 모음 - (칸의 좌표, 움직인 횟수) 형태로 저장
    que = deque([(start,0)])
    
    # 5.탐색
    while que:
        # 좌표, 움직인 횟수 꺼내기
        (r,c), cnt = que.popleft()
        
        # 꺼낸 좌표가 목표지점이라면?
        if (r,c) == end:
            return cnt
        
        # 목표 지점이 아니라면? -> 모든 방향으로 미끄러지면서 이동
        for dr, dc in directions:
            # (nr,nc) 벽에 멈추기 직전에 멈춘 곳의 좌표
            # 한 칸 이동하자마자 벽에 부딪혔을 때를 대비
            nr = r
            nc = c
            
            # 한 칸 더 가도 되는지 확인
            while 0 <= nr + dr < n and 0 <= nc + dc < m and board[nr + dr][nc+dc] != "D":
                nr = nr + dr
                nc = nc + dc
        
            # 멈춘 칸이 방문했던 칸이 아니라면?
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                que.append(((nr, nc),cnt+1))
    
    # 6.끝까지 못찾았다면?
    return -1