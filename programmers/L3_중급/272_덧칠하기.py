# 덧칠하기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 알고리즘: 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 28. 19:30:09

def solution(n, m, section):
    """
    n: 페인트가 칠해진 벽의 길이
    m: 벽에 페인트를 칠할 때 사용하는 롤러의 길이(m<=n)
    section:페인트를 다시 칠해야 하는 구역
    
    
    구역의 일부분만 포함되는 것은 안됨
    
    구역에 번호를 붙이는 규칙:  1, 2, 3, ...., n
    """
    # 페인트를 다시 칠해야 하는 영역과 그렇지 않은 영역을 1차원 지도로 기록
    walls = [1] * (n+1) # 0번 벽은 사용할 일 없음
    
    for s in section:
        walls[s] = 0
        
    # 페인트질 횟수
    answer = 0
    for i in range(1,n+1):
        if walls[i] == 0:
            answer += 1
            for j in range(i,min(i+m, n+1)):
                # 벽에서 벗어나는 것을 방지하기 위해 n번 이상의 벽을 칠하게 되는 상황을 막고자 함
                walls[j] = 1
                
    return answer