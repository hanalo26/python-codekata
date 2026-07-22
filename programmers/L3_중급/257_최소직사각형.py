# 최소직사각형
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 알고리즘: 완전탐색, 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 22. 14:12:53

def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        # w,h 중에서 더 짧은 쪽을 h_side, 더 긴 쪽을 w_side로 정의
        w_side = max(w,h)
        h_side = min(w,h)
        
        # max_w, max_h와 비교해서 더 큰 값을 max_w, max_h로 저장
        max_w = max(max_w, w_side)
        max_h = max(max_h, h_side)
    
    answer = max_w * max_h
    
    return answer