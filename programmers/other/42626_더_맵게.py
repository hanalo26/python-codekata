# 더 맵게
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 작성자: 백하은
# 작성일: 2026. 07. 24. 01:23:09

# 서로 다른 음식을 섞어서 만든 음식의 스코빌 지수
# = 가장 안 매운 음식 + 두번째로 안 매운 음식*2

# 섞는 음식을 선정하는 기준
# 스코빌 지수가 가장 낮은 것, 두번째로 낮은 것

# 모든 원소의 값이 K이상이 되면 stop

# 모든 음식을 다 섞어도 K이상이 될 수 없다면 -1

# 음식을 섞을 때마다 return해야 하는 값은 +1

import heapq

def solution(scoville, K):
    # 음식을 섞은 횟수
    cnt = 0
    
    # 최소값이 자동으로 맨 앞으로 오는 자료형으로 변환
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        # 더이상 섞을 음식이 없다면..? -> 남은 음식이 2미만
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville) # 남은 것 중에 가장 안 매운 음식
        second = heapq.heappop(scoville) # 남은 것 중에 두번째로 안 매운 음식
        
        n = first + 2 * second
        
        heapq.heappush(scoville, n)
        cnt += 1
        
    return cnt