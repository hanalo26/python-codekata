# 최소직사각형
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 알고리즘: 완전탐색, 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 24. 16:14:51

def solution(sizes):
    # 제작할 지갑의 w,h
    max_w = 0
    max_h = 0
    
    # 각 명함들의 가로/세로 정하기
    for w,h in sizes:
        name_w = max(w,h)
        name_h = min(w,h)
        
        max_w = max(max_w, name_w)
        max_h = max(max_h, name_h)
        
    return max_w * max_h