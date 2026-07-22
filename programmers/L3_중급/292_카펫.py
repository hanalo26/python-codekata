# 카펫
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 23. 00:03:58

# 중앙은 노란색, 테두리는 갈색인 카펫이 만들어짐

def solution(brown, yellow):
    # 전체 칸의 개수(total)
    total = brown + yellow
    
    # total = w*h인 정수 w와 h 찾기
    # 조건 1. 가로 >= 세로
    # 조건 2. 노란색이 한 줄짜리일때, 이를 감싸기 위해서는 최소 높이 3이 필요함
    for h in range(3,total+1):
        if total % h == 0:
            w = total // h
            
            # 가운데에 있는 노란 블록은 최소 테두리가 하나씩 양쪽에 존재하므로 yellow = (w-2)*(h-2)가 되어야 함
            if w >= h and (w-2)*(h-2) == yellow:
                return [w,h]