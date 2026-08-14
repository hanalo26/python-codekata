# 기능개발
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 알고리즘: 스택/큐
# 작성자: 백하은
# 작성일: 2026. 08. 14. 16:19:41

import math

def solution(progresses, speeds):
    answer = [] # 한 번에 배포되는 기능의 개수
    
    # 각 기능별 잔여 작업일수
    day = []
    
    for p, s in zip(progresses, speeds):
        d = math.ceil((100-p)/s)
        day.append(d)
    
    # 그룹화
    stand = day[0]
    cnt = 0 # 해당 순서에 배포되는 기능의 개수
    
    for d in day:
        if d <= stand:
            cnt += 1
        else:
            answer.append(cnt)
            stand = d
            cnt = 1
            
    # 마지막 배포 그룹도 결과에 추가
    answer.append(cnt)
    
    return answer