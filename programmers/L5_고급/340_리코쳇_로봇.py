# 리코쳇 로봇
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 알고리즘: BFS
# 작성자: 백하은
# 작성일: 2026. 07. 23. 16:58:55

from collections import deque

def solution(board):
    # 1. 격자의 크기는?
    n = len(board) # 행
    m = len(board[0]) # 열
    
    # 2. 시작지점과 목표지점은?
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j)
            if board[i][j] == "G":
                goal = (i,j)
    
    # 3. 미끄러져서 로봇이 서있는 지점 기록, 상하좌우로 움직인 횟수 등을 기록하기 위한 변수 정의 + 이동을 위한 방향키 설정
    # 방향키(상하좌우 순서대로)
    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    
    # 방문여부 기록용
    visited = {start}
    
    # 좌표 및 이동횟수 기록용
    q = deque([(start,0)])
    
    # 4. 탐색 (탐색 중에 목표지점에 도달하면 종료)
    while q:
        (r,c),cnt = q.popleft()
        
        # (r,c)가 목표 지점일 때
        if (r,c) == goal:
            return cnt
        
        # (r,c)가 목표 지점이 아닐 떄
        for dr, dc in directions:
            # 한 칸 이동하자마자 벽이나 장애물에 부딪혔을 떄
            nr = r
            nc = c
            
            # 한 칸 이동했을 때 벽이나 장애물에 부딪히지 않았을 때 -> 부딪힐 때까지 이동
            while 0 <= nr+dr < n and 0 <= nc+dc < m and board[nr+dr][nc+dc] != "D":
                nr = nr+dr
                nc = nc+dc
                
            # 방문했다고 기록되지 않은 칸이라면?
            if (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append(((nr,nc),cnt+1))
    
    # 5. 만약에 끝까지 목표지점을 만나지 못한다면?
    return -1