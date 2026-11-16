# 광물 캐기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 알고리즘: 그리디, 완전탐색
# 작성자: 백하은
# 작성일: 2026. 11. 16. 16:46:53

"""
[문제 핵심 조건 및 규칙 정리]
1. 곡괭이 종류와 소모 피로도:
   - 다이아몬드 곡괭이: 다이아(1), 철(1), 돌(1)
   - 철 곡괭이       : 다이아(5), 철(1), 돌(1)
   - 돌 곡괭이       : 다이아(25), 철(5), 돌(1)
2. 규칙:
   - 각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에 망가지므로, 곡괭이 하나로 5개를 연속으로 캐야 함
   - 광물은 주어진 순서대로만 캘 수 있음
   - 가진 곡괭이를 모두 쓰거나, 광산을 다 캐면 종료
3. 최적화 전략 (Greedy):
   - 가치가 높은 광물이 많이 포함된 5개 묶음일수록, 가장 좋은 곡괭이(다이아 곡괭이)를 먼저 써야 피로도를 최소화할 수 있음
   -> 5개씩 광물 묶음을 나누어 (다이아 개수, 철 개수, 돌 개수) 기준으로 내림차순 정렬한 뒤 좋은 곡괭이부터 차례대로 배정
"""

def solution(picks, minerals):
    # 1단계: 가지고 있는 모든 곡괭이의 개수를 더해서, 총 몇 개의 묶음(5개씩)을 캘 수 있는지 계산
    total_picks = sum(picks)
    max_minerals = total_picks * 5
    
    # 만약 광물이 곡괭이로 캘 수 있는 양보다 많다면, 
    # 곡괭이로 감당할 수 있는 만큼의 광물만 남기고 삭제
    if len(minerals) > max_minerals:
        minerals = minerals[:max_minerals]
        
    # 2단계: 광물을 5개씩 묶어서 어떤 광물들이 들어있는지 확인
    # 왜냐하면 5개씩 묶음을 지어서 '다이아몬드가 몇 개 있는지' 파악해야 어떤 곡괭이를 먼저 쓰는 것이 이득인지 판단할 수 있음
    mineral_groups = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5] # 5개씩 자르기
        
        dia_cnt = 0
        iron_cnt = 0
        stone_cnt = 0
        
        # 묶음 안에서 광물의 개수를 셈
        for m in chunk:
            if m == "diamond":
                dia_cnt += 1
            elif m == "iron":
                iron_cnt += 1
            else:
                stone_cnt += 1
                
        # (다이아몬드 개수, 철 개수, 돌 개수) 형태로 리스트에 저장
        mineral_groups.append((dia_cnt, iron_cnt, stone_cnt))
        
    # 3단계: 중요한 광물(다이아몬드 > 철 > 돌 순서)이 많이 포함된 묶음일수록 "좋은 곡괭이(다이아몬드 곡괭이)"를 먼저 써야 피로도를 아낄 수 있음
    # 따라서 다이아몬드가 많은 순서, 철이 많은 순서대로 묶음들을 정렬(내림차순)
    mineral_groups.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    
    # 4단계: 피로도 총합을 저장할 변수를 0으로 초기화
    total_fatigue = 0
    
    # 5단계: 정렬된 묶음들을 순서대로 확인하면서 가장 좋은 곡괭이부터 차례대로 사용
    for dia, iron, stone in mineral_groups:
        
        # 다이아몬드 곡괭이가 남아있다면? 가장 비싼 곡괭이를 먼저 사용
        if picks[0] > 0:
            picks[0] -= 1 # 다이아몬드 곡괭이 1개 소모
            # 다이아몬드 곡괭이는 어떤 광물이든 캐는 데 피로도가 1씩 듭니다. (광물 개수 = 5개)
            total_fatigue += (dia * 1) + (iron * 1) + (stone * 1)
            
        # 다이아몬드 곡괭이가 없고 철 곡괭이가 남아있다면? 철 곡괭이 사용
        elif picks[1] > 0:
            picks[1] -= 1 # 철 곡괭이 1개 소모
            # 철 곡괭이는 다이아 캐면 5, 철은 1, 돌은 1의 피로도 소모
            total_fatigue += (dia * 5) + (iron * 1) + (stone * 1)
            
        # 다이아, 철 곡괭이가 모두 없고 돌 곡괭이만 남아있다면? 돌 곡괭이를 씁니다.
        elif picks[2] > 0:
            picks[2] -= 1 # 돌 곡괭이 1개 소모
            # 돌 곡괭이는 다이아 캐면 25, 철은 5, 돌은 1의 피로도 소모
            total_fatigue += (dia * 25) + (iron * 5) + (stone * 1)
            
        # 만약 쓸 수 있는 곡괭이가 아예 없다면 반복을 멈춤
        else:
            break
            
    # 6단계: 계산된 최소 피로도 총합 반환
    return total_fatigue