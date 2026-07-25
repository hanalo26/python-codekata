# 기능개발
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 07. 25. 19:17:52

import math

def solution(progresses, speeds):
    # 1. 기능별 작업 완료 시간 계산
    times = []
    
    for p, s in zip(progresses, speeds):
        time = math.ceil((100-p)/s)
        
        times.append(time)
    
    # 2. 기능 배포 기준, 한 번에 배포되는 기능의 개수
    standard = times[0]
    
    num_of_progress = 1
    
    answer = []
    
    # 3. 현재 작업진행도에다가 하루 작업속도를 적용해 작업이 완료되는 일수 계산
    # -> 앞에 있는 작업이 완료되어야 뒤에 있는 작업 배포 가능
    # -> 뒤에 있는 작업이 배포 기준이 되는 작업보다 늦게 완료되면 따로 배포해야 함
    for t in times[1:]:
        if t <= standard:
            num_of_progress += 1
        
        else:
            answer.append(num_of_progress)
            standard = t
            num_of_progress = 1
            
    # 마지막으로 배포되는 것은 answer에 추가하지 않음(실수-> 추가하는 것으로 수정 완료)
    answer.append(num_of_progress)
    
    # 최종 답
    return answer