# 카펫
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 24. 18:06:51

def solution(brown, yellow):
    # 갈색이 테두리, 노란색이 중앙
    
    # 1. 카펫의 크기
    total = brown + yellow
    
    # 2. 높이에 따른 가로 계산
    # - 높이는 중앙에 노란색이 한 줄만 있을 때, 최소 3개가 필요함
    for h in range(3, total+1):
        if total % h == 0:
            w = total // h
            
            # - 가로는 항상 세로보다 길거나 같음
            if w >= h and (w-2)*(h-2) == yellow:
                return [w,h]
            
    return -1