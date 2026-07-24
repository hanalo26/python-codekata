# 리코쳇 로봇
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 알고리즘: BFS
# 작성자: 백하은
# 작성일: 2026. 07. 24. 21:14:09

# 로봇은 상하좌우로 움직임
# 로봇은 벽이나 장애물에 부딪히기 전까지 한 방향으로 이동함
# 구해야 하는 것: 목표지점에 도착하기 위해 움직여야 하는 횟수
## 단, 도착할 수 없다면 -1 반환
from collections import deque

def solution(board):
    # 격자의 크기
    n = len(board)
    m = len(board[0])
    
    # 출발지점과 목표지점 위치 정의
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j)
            elif board[i][j] == "G":
                goal = (i,j)
    
    # 상하좌우 이동을 위한 좌표 []
    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    
    # 방문한 점을 기록하는 {}
    visit = {start}
    
    # 현재 위치, 이동 횟수를 기록하는 que
    que = deque([(start,0)])
    
    # 반복문
    while que:
        # 현재 위치와 이동횟수를 꺼낼 것
        (r, c), cnt = que.popleft()
        
        # que에서 꺼낸 좌표가 목표지점인지 확인
        if (r,c) == goal:
            return cnt
        
        # 목표지점이 아니라면?
        for dr, dc in directions:
            # 한 칸만 이동하고 벽이나 장애물에 막힐 수 있음
            nr = r
            nc = c
            
            # 한 칸 더 이동해도 되는지 확인
            while 0 <= nr + dr < n and 0 <= nc + dc < m and board[nr + dr][nc + dc] != "D":
                nr = nr + dr
                nc = nc + dc
            
            # 움직인 점의 좌표를 {}에 기록하고, que에 담음(단, 방문 이력이 없는 칸이어야 함)
            if (nr,nc) not in visit:
                visit.add((nr,nc))
                que.append(((nr,nc),cnt+1))

    
    # 끝까지 목표지점을 만나지 못한 경우
    return -1