# 캐릭터의 좌표
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120861
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 26. 16:24:28

def solution(keyinput, board):
    # 이동방향 정의
    moves = {
        'up': [0,1],
        'down': [0,-1],
        'right': [1,0],
        'left': [-1,0]
    }
    
    # board의 최대/최소값
    # 버림 연산자(//) 사용
    limit_x = board[0] // 2
    limit_y = board[1] // 2
    
    # 캐릭터의 현재 위치 초기화
    x = 0
    y = 0
    
    for key in keyinput:
        dx, dy = moves[key]
        
        if abs(x+dx) <= limit_x and abs(y+dy) <= limit_y:
            x += dx
            y += dy
        
    return [x,y]