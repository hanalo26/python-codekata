# 행렬 테두리 회전하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77485
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 10. 23. 12:27:29

"""
[문제의 조건 정리]
1. 행렬 초기화
(1) 세로 rows, 가로 columns 크기의 2차원 격자에 1부터 차례대로 숫자를 채움
(2) (i, j) 위치의 초기 값은 공식으로 표현하면 (i - 1) * columns + j가 됨

2.회전 규칙 (x1, y1, x2, y2):
- 지정된 직사각형 범위의 테두리에 있는 숫자들을 시계 방향으로 한 칸씩 밀어냄

3. 결과
- 각 회전이 일어날 때마다 움직인 숫자들 중 가장 작은 숫자를 골라 순서대로 리스트에 담아 반환할 것

"""

def solution(rows, columns, queries):
    # 1부터 rows * columns까지의 숫자가 담긴 2차원 행렬 생성
    matrix = [[(r*columns)+c+1 for c in range(columns)] for r in range(rows)]
    answer = []
    
    # 각 회전(query)마다 테두리를 시계 방향으로 회전
    for x1, y1, x2, y2 in queries:
        # 문제의 좌표는 1부터 시작하므로, 파이썬 인덱스(0부터 시작)에 맞게 1씩 빼고 계산
        r1= x1 - 1
        c1 = y1 - 1
        r2 = x2 - 1
        c2 = y2 -1
        
        # 회전을 시작하기 전에 첫 번째 칸의 값을 따로 저장
        # (시계 방향으로 밀 때 첫 값이 덮어씌워져 사라지는 것을 방지하기 위함)
        start_value = matrix[r1][c1]
        min_value = start_value
        
        # 테투리 회전 시뮬레이션 시작
        # - 총 4개 변을 거꾸로 거슬러 올라가며 한 칸씩 당겨서 가져옴
        # ① 왼쪽 세로 변 (아래 -> 위)
        for r in range(r1, r2):
            matrix[r][c1] = matrix[r + 1][c1]
            min_value = min(min_value, matrix[r][c1])
            
        # ② 아래쪽 가로 변 (오른쪽 -> 왼쪽)
        for c in range(c1, c2):
            matrix[r2][c] = matrix[r2][c + 1]
            min_value = min(min_value, matrix[r2][c])
            
        # ③ 오른쪽 세로 변 (위 -> 아래)
        for r in range(r2, r1, -1):
            matrix[r][c2] = matrix[r - 1][c2]
            min_value = min(min_value, matrix[r][c2])
            
        # ④ 위쪽 가로 변 (왼쪽 -> 오른쪽)
        for c in range(c2, c1 + 1, -1):
            matrix[r1][c] = matrix[r1][c - 1]
            min_value = min(min_value, matrix[r1][c])
        # 따로 저장해둔 시작 값을 마지막 빈 칸인 '위쪽 가로의 2번째 칸'에 입력
        matrix[r1][c1 + 1] = start_value
        
        # 이번 회전에서 발견된 최소값을 결과 리스트에 추가
        answer.append(min_value)
    
    return answer