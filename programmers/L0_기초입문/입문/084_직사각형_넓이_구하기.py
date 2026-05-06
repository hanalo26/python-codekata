# 직사각형 넓이 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120860
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 06. 21:28:45

def solution(dots):
    a = dots[0]
    b = dots[1]
    c = dots[2]
    d = dots[3]
    
    # 가로
    width = max(a[0], b[0], c[0], d[0]) - min(a[0], b[0], c[0], d[0])
    
    # 세로
    height = max(a[1], b[1], c[1], d[1]) - min(a[1], b[1], c[1], d[1])
    
    # 넓이
    answer = width * height
    
    return answer