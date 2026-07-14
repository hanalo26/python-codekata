# 정수를 나선형으로 배치하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 14. 11:24:04

def solution(n):
    # n x n 크기의 빈 행렬을 [0]으로 채움
    matrix = [[0]*n for _ in range(n)]
    
    # 시계방향 -> 우,하,좌,상 방향에 따른 행열 이동 변화량 정의
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    # 초기 위치 및 시작 방향
    r = 0
    c = 0
    dir_idx = 0
    
    # 행렬 채우기
    for num in range(1,n*n+1):
        matrix[r][c] = num
    
        # 다음에 이동할 위치 계산
        next_r = r + dr[dir_idx]
        next_c = c + dc[dir_idx]
        
        # 방향을 바꿔야 하는 조건 확인
        if not (0 <= next_r < n and 0 <= next_c < n) or (matrix[next_r][next_c] != 0):
            # 방향을 90도 회전하는 효과
            dir_idx = (dir_idx+1)%4
        
        # 진짜 채워넣기
        r += dr[dir_idx]
        c += dc[dir_idx]
        
    return matrix