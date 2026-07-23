# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 백하은
# 작성일: 2026. 07. 23. 19:48:41

def solution(triangle):
    # 꼭대기에 있는 값은 높이가 1인 삼각형의 최댓값
    h = len(triangle)
    
    # i: 삼각형의 높이
    # i=0이면 음수 인덱스가 생겨 맨 마지막 줄을 더하게 되므로 반드시 1부터 시작해야 함
    for i in range(1,h):
        
        n = len(triangle[i])
        
        # j: 특정 높이 내에 있는 숫자들의 인덱스
        for j in range(n):
            
            # j가 0번 인덱스일때, 직전 행 가장 앞에 있는 원소를 더함
            if j == 0: 
                triangle[i][j] += triangle[i-1][0]
            
            # j가 n-1번 인덱스일때, 직전 행 제일 마지막에 있는 원소를 더함
            elif j == n-1:
                triangle[i][j] += triangle[i-1][-1]
            
            # j가 1 ~ n-2번 사이 인덱스일떄
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    # 정답
    return max(triangle[-1])