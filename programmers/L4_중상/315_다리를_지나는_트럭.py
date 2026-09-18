# 다리를 지나는 트럭
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 알고리즘: 스택/큐, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 09. 18. 15:12:58

from collections import deque


# 다리에 올라갈 수 있는 트럭 수: bridge_length
# 다리가 견딜 수 있는 무게: weight
# 트럭 별 무게: truck_weights
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 다리에 올라가기 위해 대기하고 있는 트럭 목록
    trucks = deque(truck_weights)
    
    # 현재 다리 위에 올라와 있는 트럭 수
    bridge = deque([0] * bridge_length)
    
    # 현재 다리를 지나가고 있는 트럭의 총 무게
    current_weight = 0
    
    # 다리 위와 대기 목록에 트럭이 남아있을 때까지 반복
    while bridge:
        # 매 루프마다 시간은 1초씩 흐름
        answer += 1
        
        # 맨 앞(다리를 다 건넌) 트럭 또는 빈 공간(0)을 제거하고 현재 무게에서 뺌
        exited_truck = bridge.popleft()
        current_weight = current_weight - exited_truck
        
        # 트럭이 아직 대기중인 경우
        if trucks:
            # 다리의 무게 제한 확인
            if current_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                # 견딜 수 없다면: 빈 공간(0)을 채워 넣어서 기존 트럭들만 앞으로 한 칸 이동
                bridge.append(0)
    
    return answer