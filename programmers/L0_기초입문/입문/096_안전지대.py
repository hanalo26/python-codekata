# 안전지대
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 05. 21:52:15

def solution(board):
    n = len(board)
    
    # 가상의 지도 생성 - 폭탄과 위험지역 체크용
    danger = [[0]*n for _ in range(n)]
    
    # "폭탄 주변 8칸 = 위험지역" 탐색을 위한 상대 좌표
    direction = [
        (-1,-1), (-1,0),(-1,1),
        (0,-1), (0,0), (0,1),
        (1,-1), (1,0), (1,1)
    ]
    
    # 폭탄 찾기
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc
                    # board 공간 내에 있는지 확인 (board의 offset 기준)
                    if 0 <= nr < n and 0 <= nc < n:
                        danger[nr][nc] = 1
                        
                        
    # danger에서 0인 칸의 수 세기
    safe_zone = 0
    for row in danger:
        safe_zone += row.count(0)
        
    return safe_zone