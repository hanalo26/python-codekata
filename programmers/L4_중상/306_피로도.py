# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 백하은
# 작성일: 2026. 07. 22. 19:53:25

def solution(k, dungeons):
    # 초기값 설정
    # 플레이어가 탐험할 수 있는 던전의 수
    answer = -1 # 디버깅을 위해 절대 나올 수 없는 수로 정의
    
    # 전체 던전의 수
    n = len(dungeons)
    
    # 던전 방문 여부
    visit = [False] * n
    
    # 각 조합별로 몇 개의 던전 탐색이 가능한지 탐색
    # 현재 피로도(current_k)
    # 지금까지 탐험한 던전의 수(cnt) 
    def dfs(corrent_k, cnt):
        # 최대 탐험 가능한 던전의 수(max_cnt)
        max_cnt = cnt
        
        # 각 던전별로 진입할 수 있는지 확인
        # 1. 각 던전별로 진입 조건, 소모되는 k 확인
        for i in range(n):
            min_k, used_k = dungeons[i]
            
            # 2. 이미 방문한 곳이 아니고, 진입 조건을 만족하는지 확인
            if (not visit[i]) and (corrent_k >= min_k):
                # 조건을 만족한다면 방문했다고 표시
                visit[i] = True
                
                # 피로도는 깎이고, 탐험한 던전 수는 +1
                result = dfs(corrent_k-used_k, cnt+1)
                
                # 3. 탐험한 최대 던전 수 갱신
                max_cnt = max(result, max_cnt)
                
                # 4. 던전 방문 여부 초기화
                visit[i] = False
                
        # 최대 던전 수 return
        return max_cnt
    
    # dfs() 함수를 활용한 값 return
    return dfs(k,0)                