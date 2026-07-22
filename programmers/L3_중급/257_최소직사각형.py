# 최소직사각형
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 알고리즘: 완전탐색, 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 22. 23:37:07

def solution(sizes):
    # 지갑의 가로,세로 길이
    max_w = 0 # 가로
    max_h = 0 # 세로
    
    for w,h in sizes:
        # 명함을 돌려서 넣는 것도 가능하므로
        w_side = max(w,h)
        h_side = min(w,h)
        
        # 지값의 크기 갱신
        max_w = max(max_w, w_side)
        max_h = max(max_h, h_side)
        
    return max_w * max_h