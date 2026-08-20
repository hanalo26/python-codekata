# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 백하은
# 작성일: 2026. 08. 20. 14:09:48

def solution(k, dungeons):
    # 도전할 수 있는 던전의 수
    n = len(dungeons)
    
    # 특정 던전 방문 여부
    visit = [False] * n
    
    # 각 던전별 클리어 가능 여부 탐색
    ## cur_k : 던전에 진입하기 전 보유한 피로도
    ## cnt : 직전까지 클리언한 던전의 수
    def dfs(cur_k, cnt):
        
        max_cnt = cnt
        
        # 던전별로 클리어 가능 여부 확인
        for i in range(n):
            min_k, used_k =  dungeons[i]
            
            # 진입 조건 만족 여부 검사
            if (not visit[i]) and (cur_k >= min_k):
                visit[i] = True
                
                # 던전 클리어 후
                result = dfs(cur_k-used_k, cnt+1)
                
                # 던전 수 갱신
                max_cnt = max(max_cnt, result)
                
                # 던전 방문 여부 초기화
                visit[i] = False
                
        return max_cnt
    
    return dfs(k,0)