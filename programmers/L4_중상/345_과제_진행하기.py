# 과제 진행하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 알고리즘: 스택, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 11. 21. 17:12:12

"""
[문제 핵심 조건 및 규칙 정리]
1. 입력 데이터 변환 및 정렬:
   - plans의 원소는 [과제명, 시작시각("hh:mm"), 걸리는시간(분)]
   - 계산을 쉽게 하기 위해 시작시각을 '분' 단위 정수로 변환 (예: "12:20" -> 12*60 + 20 = 740분)
   - 시작시각이 빠른 순서대로 정렬(모든 시작시각은 서로 다름)
2. 과제 진행 규칙:
   - 새 과제를 시작할 시각(next_start)이 되면 기존 과제를 멈추고 새 과제를 시작
   - 멈춘 과제는 '가장 최근에 멈춘 과제'부터 다시 시작 => stack 사용
   - 현재 과제를 끝낸 뒤 다음 과제 시작까지 시간이 남는다면, 남은 시간만큼 멈춰둔 과제를 이어서 진행
   - 끝나는 시각과 새 과제 시작 시각이 같으면 현재 과제를 먼저 끝낸 것으로 처리

[구해야 하는 것]
- 과제를 끝낸 순서대로 과제 이름을 담은 리스트를 반환
"""
# 시작시각을 '분' 단위 정수로 변환하는 보조 함수
def to_minutes(time_str):
    hours, mins = map(int, time_str.split(":"))
    
    return hours * 60 + mins

# 과제를 끝낸 순서대로 과제 이름을 담은 리스트를 구할 메인 함수
def solution(plans):
    # 1. [시작시각(분), 과제명, 남은시간(분)] 형태로 변환하고 시작시각 순으로 정렬
    parted = []
    for name_sbj, start_time, playtime in plans:
        parted.append([to_minutes(start_time), name_sbj, int(playtime)])
    
    parted.sort(key=lambda x: x[0])
    
    # 하다가 멈춘 과제 모음
    paused = []
    
    # 끝낸 과제 모음
    finished = []
    
    # 2. 앞 과제부터 차례대로 다음 과제 시작 시각과 비교하며 과제 시작
    for i in range(len(parted) - 1):
        cur_start, cur_sbj, cur_playtime = parted[i]
        next_start = parted[i+1][0] # 범위 설정을 len(parted)-1로 설정한 이유
        
        # 다음 과제가 시작되기 전에 현재 과제를 끝낼 수 있는 경우
        if cur_start + cur_playtime <= next_start:
            finished.append(cur_sbj)
            
            # 현재 과제를 끝내고도 다음 과제 시작까지 남은 여유 시간(분)
            spare_time = next_start - (cur_start + cur_playtime)
            
            # 여유 시간이 있고, 멈춰둔 과제도 있다면 가장 최근 멈춘 과제부터 이어서 진행
            while spare_time > 0 and paused:
                p_sbj, p_playtime = paused.pop()
                if p_playtime <= spare_time:
                    # 멈춰둔 과제를 완전히 끝낼 수 있는 경우
                    spare_time = spare_time - p_playtime
                    finished.append(p_sbj)
                else:
                    # 여유 시간 안에 다 못 끝내고 또 멈춰야 하는 경우
                    p_playtime =  p_playtime - spare_time
                    spare_time = 0
                    paused.append([p_sbj, p_playtime])
        else:
            # 다음 과제 시작 시각이 되어서 현재 과제를 중단해야 하는 경우 -> (next_start - cur_start)만큼 진행했으므로 남은 시간을 저장
            worked = next_start - cur_start
            paused.append([cur_sbj, cur_playtime - worked])
                    
    # 3. 마지막으로 시작한 과제는 뒤에 더 오는 새 과제가 없으므로 바로 완료로 처리
    finished.append(parted[-1][1])
    
    # 4. 아직 완료하지 못한 과제가 남아있다면? 최근 멈춘 과제부터 수행
    while paused:
        p_sbj, _ = paused.pop()
        finished.append(p_sbj)
    
    return finished