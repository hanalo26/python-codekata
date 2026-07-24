# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 백하은
# 작성일: 2026. 07. 24. 19:21:43

def solution(k, dungeons):
    
    # 도전할 수 있는 던전의 수
    n = len(dungeons) 
    
    # 특정 던전 방문 여부
    visit = [False] * n
    
    # 각 던전별로 클리어 가능 여부 탐색
    # current_k : 특정 던전에 진입하기 전, 피로도
    # cnt : 특정 던전에 진입하기 전까지 클리어한 던전의 수
    def dfs(current_k, cnt):
        
        # 탐험 가능한 최대 던전 수
        max_cnt = cnt
        
        # 각 던전 별로 확인
        for i in range(n):
            min_k, used_k = dungeons[i]
            
            # 이미 방문한 던전이 아니고, 진입 조건을 만족하는지 검사
            if (not visit[i]) and (current_k >= min_k):
                visit[i] = True
                
                result = dfs(current_k-used_k, cnt+1)
                
                # 최대 던전 수 갱신 
                max_cnt = max(max_cnt, result)
                
                # 던전 방문 여부 초기화
                visit[i] = False
    
        return max_cnt
    
    return dfs(k,0)