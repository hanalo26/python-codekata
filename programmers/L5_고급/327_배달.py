# 배달
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 알고리즘: 그래프, 다익스트라
# 작성자: 백하은
# 작성일: 2026. 10. 02. 18:42:19

# 마을의 개수(N)
# road (마을1, 마을2, 이동시간)
# 음식 배달이 가능한 시간(K)
# 음식점의 위치 = 마을 1

# 구하고자 하는 것: 음식 주문을 받을 수 있는 마을의 개수

def solution(N, road, K):
    
    # 1번 마을에서 각 마을로 배달하는 시간을 무한대로 설정(기본값) 
    # -> 출발지-도착지 관계로 표 생성
    INF = float('inf')
    maps = [[INF]*(N+1) for _ in range(N+1)]
    
    # 같은 마을 내에서는 이동시간이 0
    for i in range(1,N+1):
        maps[i][i] = 0
        
    # road에 저장된 정보 불러와서 표에 채워넣기
    # 단, 각 마을을 연결하는 길이 2개 이상이라면 최솟값으로 채움
    for a,b,x in road:
        maps[a][b] = min(maps[a][b], x)
        maps[b][a] = min(maps[b][a], x)
        
    # 마을간의 이동을 직접하는 것과 경유했다가 가는 것의 이동시간 비교
    #   - k: 경유하는 마을의 번호
    #   - p: 출발지
    #   - q: 도착지
    for k in range(1,N+1):
        for p in range(1,N+1):
            for q in range(1,N+1):
                if maps[p][q] > maps[p][k] + maps[k][q]:
                    maps[p][q] = maps[p][k] + maps[k][q]
                    
    # 배달 가능한 마을 수 계산
    answer = 1
    
    for n in range(2,N+1):
        if maps[1][n] <= K:
            answer += 1
            
    return answer