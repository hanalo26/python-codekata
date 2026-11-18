# 디펜스 게임
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 알고리즘: 힙, 그리디
# 작성자: 백하은
# 작성일: 2026. 11. 18. 14:19:09

"""
[문제 핵심 조건 및 규칙 정리]
1. 게임 규칙:
   - 처음에 병사 `n`명을 가지고 시작하며, 매 라운드마다 `enemy[i]` 마리의 적이 나타남
   - 남은 병사 수에서 적의 수(`enemy[i]`)만큼 소모하면 해당 라운드 clear
   - 병사가 부족하면 게임 종료
2. 무적권 스킬:
   - 병사를 소모하지 않고 한 라운드의 공격을 막아낼 수 있는 '무적권'을 최대 `k`번 사용 가능
3. 목표:
   - 무적권과 병사를 적절히 사용하여 최대한 많은 라운드를 진행하는 것
4. 알고리즘 전략 (그리디 + 최소 힙):
   - 일단 모든 적을 병사로 막는다고 가정하고 계산
   - 병사가 부족해지는 순간, {지금까지 막았던 라운드 중 적이 가장 많았던 곳}에 무적권을 씁니다!
   -> 무적권은 적이 가장 많이 몰려온 곳에 소급해서 사용하는 것이 가장 이득
"""
import heapq

def solution(n, k, enemy):
    # 1. 지금까지 상대한 적의 수를 담아둘 '최소 힙' 리스트
    played_enemies = []
    
    # 2. 라운드를 진행하며 적 소탕 시작
    for round_idx, num_of_enemies in enumerate(enemy):
        # 3. 현재 라운드의 적의 숫자만큼 병사를 소모하고, 제거한 적의 수를 played__enemies에 저장
        n = n - num_of_enemies
        # 적의 숫자에 -를 붙여서 가장 많은 적이 존재하는 라운드가 가장 작다고 heapq이 인식하도록 만듦
        heapq.heappush(played_enemies, -num_of_enemies)
        # 4. 현재 라운드를 진행하고 병사가 0명 미만이 되었다면 무적권의 존재 여부를 확인하고, 무적권도 없다면 게임은 종료됨
        if n < 0:
            if k > 0:
                # -를 붙여서 heapq에 넣었으므로, 꺼낼 때는 다시 -를 붙여서 꺼냄
                largest_battle = -heapq.heappop(played_enemies)
                # 가장 많은 적이 있던 라운드에서는 무적권을 써서 병사 소모가 없는 것으로 다시 계산
                n += largest_battle
                k = k - 1
            else:
                return round_idx
    
    # 모든 라운드를 클리어했음에도 불구하고, 병사가 남아있다면?
    return len(enemy)