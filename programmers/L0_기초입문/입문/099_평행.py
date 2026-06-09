# 평행
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 09. 21:28:17

def solution(dots):
    # 올바른 언패킹 구조: 왼쪽이 변수, 오른쪽이 데이터
    dot1, dot2, dot3, dot4 = dots
    
    # 각 점의 x, y 좌표 분리
    x1, y1 = dot1
    x2, y2 = dot2
    x3, y3 = dot3
    x4, y4 = dot4
    
    # 1-2, 3-4인 경우
    # 원래 식: (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3)
    if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
        return 1
    
    # 1-3, 2-4인 경우
    if (y3 - y1) * (x4 - x2) == (y4 - y2) * (x3 - x1):
        return 1
    
    # 1-4, 2-3인 경우
    if (y4 - y1) * (x3 - x2) == (y3 - y2) * (x4 - x1):
        return 1
    
    # 위 3가지 경우에서 모두 false, 즉 평행이 없는 경우
    return 0

    