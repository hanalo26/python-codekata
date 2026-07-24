# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 백하은
# 작성일: 2026. 07. 24. 20:49:24

# 더한 결과를 저장해야 겠다.
# 높이가 1인 삼각형의 최댓값은 꼭대기에 있는 숫자

def solution(triangle):
    # 삼각형의 높이 범위 : 1 <= h < 삼각형의 높이+1
    for i in range(1,len(triangle)):
        # 해당 높이에 존재하는 숫자의 개수(j)
        n = len(triangle[i])
        
        for j in range(n):
            
            # 가장 왼쪽에 있는 원소라면?
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            
            # 가장 오른쪽에 있는 원소라면?
            elif j == n-1:
                triangle[i][j] += triangle[i-1][-1]
            
            # 중간에 있는 원소라면
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])