# 기능개발
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 07. 23. 22:33:48

# progresses에서 앞에 있는 작업 진도가 100이 되어야 뒤에 있는 작업도 배포 가능
# 각 작업은 하루에 speeds에 담긴 만큼만 진행된다.
# 소요 일수는 올림으로 계산해야 한다.

# 소요 일수를 계산해서 리스트에 담아두어야겠다.
# - 뒤에 있는 요소가 바로 앞에 있는 요소보다 크면 그 작업은 같이 배포할 수 없으므로 다음 배포일의 기준이 됨
import math

def solution(progresses, speeds):
    # 1. 작업별 작업 시간 계산
    times = []
    
    for p, s in zip(progresses, speeds):
        t = math.ceil((100-p)/s)
        
        times.append(t)
    
    # 2. 가장 앞에 있는 작업 시간을 기준으로 그거보다 크면 그 앞에서 잘라서 한 번에 배포하고, 다음 배포 기준은 잘린 원소가 된다.
    answer = []
    
    standard = times[0]
    
    num_of_progress = 1
    
    for j in times[1:]:
        if j <= standard:
            num_of_progress += 1
        
        else:
            answer.append(num_of_progress)
            standard = j
            num_of_progress = 1 # 동시에 배포되는 작업 수 초기화
            
    
    # 3. 마지막 블록은 기준보다 큰 요소가 등장하지 않았으므로 수동으로 append함
    answer.append(num_of_progress)
    
    return answer