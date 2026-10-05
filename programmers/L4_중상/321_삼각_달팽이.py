# 삼각 달팽이
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 10. 05. 16:10:26

def solution(n):
    # n x n 크기의 2차원 배열 정의 (삼각형을 그릴 예정)
    triangle = [[0] * i for i in range(1,n+1)]
    
    # 방향키 (위쪽 대각선, 오른쪽 아래 대각선(아래+오른쪽 이동))
    # 아래, 오른쪽, 위쪽 대각선 순서대로 배열
    dx = [1,0,-1]
    dy = [0,1,-1]
    
    # 초기 위치
    x,y = 0,0
    num = 1 # 초기 위치에 채울 값
    direction = 0
    
    # n x n 크기의 2차원 배열에 숫자 채우기
    # 1. 아래로 내려가면서 숫자 채움
    # 2. 오른쪽이로 이동하면서 숫자 채움
    # 3. 대각선 위로 이동하면서 채우가
    # 4. 아래로 내려오면서 채우기
    for j in range(n,0, -1):
        # 현재 방향으로 j번 만큼 숫자를 적음
        for _ in range(j):
            triangle[x][y] = num
            num += 1
            x += dx[direction]
            y += dy[direction]
            
        # j번 이동 후, 경계를 1칸 벗어나게 되므로 1칸 되돌리고, 방향 전환
        x -= dx[direction]
        y -= dy[direction]
        direction = (direction+1)%3 # 0 ~ 2를 순환하도록 하기 위해
    
        # 다음 방향의 시작 위치로 이동
        x += dx[direction]
        y += dy[direction]
    
    # 2차원 리스트를 1차원 리스트로 변환
    answer = []
    
    for r in triangle:
        for val in r:
            answer.append(val)
    
    return answer