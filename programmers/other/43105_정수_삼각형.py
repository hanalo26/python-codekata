# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 백하은
# 작성일: 2026. 07. 24. 01:36:22

def solution(triangle):
    
    # 삼각형의 높이, h
    h = len(triangle)
    
    # i-1이 계산에 포함되므로 h는 1부터 시작
    # i는 검사할 삼각형의 높이
    for i in range(1,h):
        n = len(triangle[i]) # 해당 높이에 있는 원소의 개수
        
        for j in range(n):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][0]
            elif j == n-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    
    # 최종 답
    return max(triangle[-1])