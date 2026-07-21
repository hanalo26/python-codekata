# 힌트 스테이지
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468377
# 작성자: 백하은
# 작성일: 2026. 07. 21. 19:31:58

from collections import defaultdict

def solution(cost, hint):
    n = len(cost) # 전체 스테이지 수
    
    # dp[stage_idx][hints_tuple] = 최소 비용
    # hints_tuple: (0번 힌트 개수, 1번 힌트 개수,..., n-1번 힌트 개수)
    dp = {tuple([0]*n):0} # (스테이지별 힌트권):누적비용
    
    for i in range(n):
        # next_dp: $i$번째 스테이지를 클리어한 후 만들어질 "다음 힌트 상태별 최소 비용"을 저장할 공간(기본값은 inf)
        next_dp = defaultdict(lambda:float('inf'))
        
        # (힌트 보유 상태, 그때까지의 누적 비용) 조합별로 확인
        for hints, current_cost in dp.items():
            # i번째 스테이지에서 사용할 수 있는 힌트권 개수
            use_cnt = hints[i]
            # 사용 개수는 n-1개를 넘을 수 없으며, cost[i]의 길이 범위를 벗어나지 않도록 클램핑
            use_cnt = min(use_cnt, len(cost[i]) - 1)
            
            stage_cost = cost[i][use_cnt]
            
            # 선택 1: i번째 스테이지에서 힌트를 구매하지 않는 경우
            new_hints = list(hints)
            new_hints[i] = 0
            next_dp[tuple(new_hints)] = min(next_dp[tuple(new_hints)], current_cost + stage_cost)
            
            # 선택 2: i번째 스테이지에서 힌트 번들을 구매하는 경우 (마지막 스테이지 제외)
            if i < n - 1:
                bundle_price = hint[i][0]
                added_hints = hint[i][1:]
                
                buy_hints = list(hints)
                buy_hints[i] = 0
                for h_num in added_hints:
                    # 힌트권 번호는 1-based 이므로 index로 변환 (h_num - 1)
                    buy_hints[h_num - 1] += 1
                    
                next_dp[tuple(buy_hints)] = min(next_dp[tuple(buy_hints)], current_cost + stage_cost + bundle_price)
                
        dp = next_dp

    return min(dp.values())