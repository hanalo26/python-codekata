# 배달
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 알고리즘: 그래프, 다익스트라
# 작성자: 백하은
# 작성일: 2026. 07. 24. 22:11:40

def solution(N, road, K):
    INF = float("inf")
    
    # 표 제작(마을간 이동시간이 담겨있음)
    dist = [[INF]*(N+1) for _ in range(N+1)]
    
    # 같은 마을간의 이동시간 = 0
    for i in range(1,N+1):
        dist[i][i] = 0
        
    # 문제조건대로 주어진 road에 기록된 마을간 시간을 표에 추가
    for a,b,c in road:
        # 혹시 예제 2처럼 동일한 마을을 연결하는 2가지 이상의 길이 있을지도 몰라서 추가
        # 처음엔 c가 저장됨
        dist[a][b] = min(dist[a][b], c)
        dist[b][a]= min(dist[b][a], c)
        
    # k는 거쳐가는 마을의 번호 
    # i,j는 각각 출발한 마을과 도착한 마을의 번호 
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                # k를 거쳐가는 이동시간과 직행 이동시간 비교
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    # 거쳐서 가는 것이 시간이 더 짧다면 이동시간에서 변경
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 1번 마을 음식점에서 K 시간 내에 배달할 수 있는 마을의 개수
    cnt = 1 # 1번 마을은 0시간 내에 배달 가능이니까!
    
    for num in range(2,N+1):
        if dist[1][num] <= K:
            cnt += 1
    
    return cnt