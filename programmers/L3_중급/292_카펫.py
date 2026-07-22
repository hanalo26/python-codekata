# 카펫
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 22. 20:56:52

def solution(brown, yellow):
    # 1.전체 칸의 개수 = 브라운+노랑
    total = brown + yellow
    
    # 2. 가로(w)*세로(h) = 전체 칸의 개수
    # (1) 가로 >= 세로
    # (2) 세로는 3 이상이 되어야 함 (내부에 있는 요소가 한 줄짜리라고 했을때, 그걸 감쌀 수 있어야 하니까)
    for h in range(3,total+1):
        # 가로가 정수가 되기 위해서는 total이 h로 나누어 떨어져야 함
        if total % h == 0:
            w = total // h
        
        # w >= h 조건과 갈색이 테두리라고 할 때, 내부에 감싸진 노란색 블럭의 개수가 같은 값인지 확인
            if w >= h and (w-2)*(h-2) == yellow:
                return [w,h]