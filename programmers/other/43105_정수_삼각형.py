# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 백하은
# 작성일: 2026. 07. 23. 19:35:03

def solution(triangle):
    # 높이가 1이면 꼭대기의 값 = 최대값 (인덱스로는 0)
    h = len(triangle)
    
    for i in range(1,h): # i: 해당 숫자 배열이 위치한 높이 
        
        n = len(triangle[i])
        
        for j in range(n): # j: 숫자 배열 내에서 특정 숫자의 위치
            
            # triangle[i][j]가 가장 왼쪽에 있는 숫자일 때 (j=0)
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][0]
            
            # triangle[i][j]가 가장 오른쪽에 있는 숫자일때 (j=n-1)
            elif j == n-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][-1]
            
            # triangle[i][j]가 가운데에 있는 숫자일때
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
                
    # 마지막 줄에서 가장 큰 값을 반환 = 구하고자 하는 값            
    return max(triangle[-1])