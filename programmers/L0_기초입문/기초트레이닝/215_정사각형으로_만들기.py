# 정사각형으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181830
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 13. 11:54:05

def solution(arr):
    rows = len(arr) # 행의 개수
    cols = len(arr[0]) # 열의 개수
    
    # 행의 개수 > 열의 개수
    if rows > cols:
        diff = rows - cols
        for r in arr:
            # 기존 행 뒤에 부족한 만큼 0을 채움
            r.extend([0]*diff)
            
    # 행의 개수 < 열의 개수
    if rows < cols:
        diff = cols - rows
        for _ in range(diff):
            # 모든 열의 길이를 커버할 수 있는 0번 행을 아래에 추가
            arr.append([0]*cols)
            
    # 행의 개수 = 열의 개수
    return arr