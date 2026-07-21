# 선인장 숨기기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468379
# 작성자: 백하은
# 작성일: 2026. 07. 21. 18:35:28

def solution(m, n, h, w, drops):
    # 비가 오지 않는 칸은 inf, 즉 무한대로 둠 (기본값으로 작용하도록 설정)
    INF = float('inf')
    # 비가 내리는 시간 기록
    grid = [[INF]*n for _ in range(m)] # INF가 원소인 grid 생성
    for time_idx, (r,c) in enumerate(drops):
        grid[r][c] = time_idx
        
    # time_limit 시점까지 비를 안 맞고 버티는 h x w 구역이 있는지 확인
    def rain_check(time_limit):
        # ime_limit 이하 시간에 비가 내렸으면 1, 아니면 0
        p_sum = [[0]*(n+1) for _ in range(m+1)] # 기존 지도보다 한 칸 더 큰 것을 만들어서 2차원의 누적합 계산
        for r in range(m):
            for c in range(n):
                val = 1 if grid[r][c] <= time_limit else 0
                # 비를 맞은 칸(1)의 개수 count
                p_sum[r+1][c+1] = val + p_sum[r][c+1] + p_sum[r+1][c] - p_sum[r][c]
                
        # h x w 직사각형 내부의 합이 0인 구역(안전지대) 탐색
        best_r, best_c = -1, -1
        for r in range(h,m+1):
            for c in range(w,n+1):
                # (r-h, c-w) ~ (r-1, c-1) 영역의 비 내린 칸 수
                # 구역 내 빗방울 수 = {전체} - {위쪽 영역} - {왼쪽 영역} + {위쪽과 왼쪽 영역의 중복되는 모서리}
                rain_count = p_sum[r][c] - p_sum[r - h][c] - p_sum[r][c - w] + p_sum[r - h][c - w]

                # 비를 맞지 않는 영역이 존재하는 경우
                if rain_count == 0:
                    return True, [r-h, c-w]

        # 비를 맞지 않는 영역이 존재하지 않는 경우
        return False, []
    
    # 3. 이분 탐색 수행 (버틸 수 있는 최대 시간 K 찾기)
    low = 0
    high = len(drops) - 1
    max_safe_time = -1
    answer = [0,0] # 기본값: 첫 비부터 맞아야 할 때 (0, 0)
    
    while low <= high:
        mid = (low + high) // 2
        possible, pos = rain_check(mid)
        
        if possible:
            max_safe_time = mid
            answer = pos
            low = mid + 1  # 더 늦은 시간까지 버틸 수 있는지 확인
        else:
            high = mid - 1 # 시간을 줄여서 다시 확인
            
    # 비를 전혀 안 맞는 완벽한 구역이 존재하는 경우
    perfect_possible, pos = rain_check(INF)
    if perfect_possible:
        return pos

    return answer