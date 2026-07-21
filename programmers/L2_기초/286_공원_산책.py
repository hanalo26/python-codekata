# 공원 산책
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172928
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 21. 12:38:02

def solution(park, routes):
    # 동쪽으로 이동: (0,1)
    # 서쪽으로 이동: (0,-1)
    # 남쪽으로 이동: (1,0)
    # 북쪽으로 이동: (-1,0)
    
    H = len(park)
    W = len(park[0])
    
    # 시작점
    r = 0
    c = 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                r,c = i,j
                break
    
    # 이동방향
    directions = {
        "N": (-1,0),
        "S": (1,0),
        "W": (0,-1),
        "E": (0,1)
    }
    
    # 이동
    for route in routes:
        # op: 방향
        # n: 이동할 칸의 수 
        op, n = route.split()
        n = int(n)
        
        dr, dc = directions[op]
        
        nr, nc = r, c
        is_valid = True
        
        for _ in range(n):
            nr += dr
            nc += dc
            
            # 경계를 벗어나거나 장애물(X)을 만나는 경우 -> 실패
            if not (0 <= nr < H and 0 <= nc < W) or park[nr][nc] == "X":
                is_valid = False
                break
                
        if is_valid:
            r,c = nr, nc
            
    return [r,c]