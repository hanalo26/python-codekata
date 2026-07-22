# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 백하은
# 작성일: 2026. 07. 22. 17:42:44

def solution(k, dungeons):
    # 탐험할 수 있는 던전의 수 
    # -1은 절대 나올 수 없으므로 디버깅을 위해 초기값으로 설정
    answer = -1
    
    # 던전의 수
    n = len(dungeons)
    
    # 던전 방문 여부
    visit = [False] * n
    
    # current_k: 현재 피로도
    # cnt: 탐험한 던전 수
    def dfs(current_k, cnt):
        max_dun = cnt
        
        # 갈 수 있는 던전 탐색
        for i in range(n):
            min_k, use_k = dungeons[i]
            
            # 방문하지 않았으며, 최소 피로도 조건을 채운 경우
            if (not visit[i]) and (current_k >= min_k):
                visit[i] = True # 방문함!
                
                # 피로도 깎기, 도전한 던전은 +1
                result = dfs(current_k-use_k, cnt+1)
                max_dun = max(max_dun, result)
                
                # 도전한 던전이라는 표시 삭제
                visit[i] = False
                
        # 찾아본 줄기에서 찾은 최대 던전 수
        return max_dun
    
    return dfs(k,0)